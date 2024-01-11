# Face Recognition Door Unlock System

## Abstract
In the era of automation and smart devices, ensuring privacy and security in information systems is critical. Traditional security measures, such as mechanical locks, are limited, and there is a need for innovative solutions. The "Door Unlock using Face Recognition" project aims to enhance security by implementing a face recognition system using a Raspberry Pi and an infrared night vision camera. This system eliminates the need for traditional keys and passwords, providing a keyless and secure access control solution.

## 1. Introduction
With the widespread use of smart devices, traditional security measures need to evolve. Many conventional systems rely on mechanical locks with limitations on the number of keys. This project proposes a face recognition system to unlock doors, addressing the shortcomings of traditional security methods. By capturing and matching faces using a Raspberry Pi and infrared camera, the system ensures secure access.

## 2. Literature Survey
The project draws inspiration from existing work in face recognition and security systems. Previous research and implementations, such as those utilizing OpenCV, LBPH algorithm, and Raspberry Pi integration, have contributed to the development of this project.

## 3. Methodology
The face recognition system follows a step-by-step process, including human presence detection, face image capture, face recognition, eye blinking detection, and security actions. The system leverages the Dlib library for face recognition, detecting 68 landmarks on the face and generating unique measurements for each individual. Additionally, eye blinking detection adds an extra layer of security.

## 4. Hardware Design
The main components of the system include a Raspberry Pi, an infrared night vision camera, a DC motor for door control, and an ultrasonic sensor for human presence detection. These components work in tandem to create a robust and automated door unlocking system.

## 5. Results
The system's simulation demonstrates successful face recognition and blink detection. In scenarios where an unknown person is detected, emails are sent to the owner, a WhatsApp message alerts them of an intruder, and the door remains locked. The system provides real-time notifications and takes appropriate actions based on the detected faces.

## 6. Conclusion
The implemented system successfully unlocks the door for recognized faces, detects fake faces, and sends notifications to the owner in case of an unknown person. The combination of face recognition and additional security features enhances access control and addresses traditional security limitations.

## 7. Limitations
Challenges include potential issues with low-quality cameras affecting face detection and the processing time required for differentiating between fake and genuine faces.

## 8. Future Scope
The project has potential applications in industries with advanced technologies and can be expanded for use in museums or locker systems by integrating additional features like iris recognition.

## 9. References
Explore more about face recognition and related technologies through the provided references.

## 10. How to Use
1. Clone the repository.
2. Install the required libraries and dependencies.
3. Connect the Raspberry Pi, infrared camera, DC motor, and ultrasonic sensor.
4. Run the system and follow the prompts for setup.

Feel free to contribute and enhance the project for broader applications in security and access control.
