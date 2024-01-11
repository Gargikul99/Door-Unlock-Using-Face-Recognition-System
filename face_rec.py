import cv2
import numpy as np
import face_recognition
import os
import time
import dlib
from math import hypot
import message as m
import smtpmail as sm
import retrive as rv
import alexaa as al


path = 'images'
images = []
classNames = []
imgList = os.listdir(path)
#print(imgList)
flag = 0

for cls in imgList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
#print(classNames)

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(img, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(img, center_top, center_bottom, (0, 255, 0), 2)

    ver_line_len = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    hor_line_len = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))

    ratio = hor_line_len / ver_line_len

    return ratio



def findEncodings(imgs):
    encodeList = []
    for img in imgs:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



encodeListKnown = findEncodings(images)
#print('encoding done')

cap = cv2.VideoCapture(0)


detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x+p2.x)/2), int((p1.y+p2.y)/2)
i=0
while i < 15:
    success, img = cap.read() # non-blocking
    cv2.waitKey(100)
    cv2.imshow('INPUT', img)
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    faces=detector(img)
    for face in faces:
        landmarks = predictor(img, face)

        left_eye_ratio = get_blinking_ratio([36,37,38,39,40,41], landmarks)
        right_eye_ratio = get_blinking_ratio([42,43,44,45,46,47], landmarks)
        blinking_ratio = ( left_eye_ratio + right_eye_ratio)/2

    facesCurrFrame = face_recognition.face_locations(imgs)
    encodesCurrrFrame = face_recognition.face_encodings(imgs, facesCurrFrame)

    for encodeFace, faceLoc in zip(encodesCurrrFrame, facesCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)

        matchIndex =np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1, x2, y2, x1= faceLoc
            y1, x2, y2, x1 =y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y1 - 5), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, 'blinking', (50, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0))



            #cv2.putText(img, 'blinking', (50, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0))
            if (name) and (blinking_ratio>3):
                #print('allow')

                flag = 1
            else:
                #m.my_msg()
                cv2.waitKey(1000)
                # Save the frame
                cv2.imwrite('inputImage/capture.jpg', img)
                flag = 0


    i += 1



    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.waitKey(1)
if flag:
    al.talk("DOOR UNLOCKED, WELCOME IN")
    print("ALLOWED")

else:
    m.my_msg()
    sm.mails()
    time.sleep(20)
    rv.retirve_mail()

