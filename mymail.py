import credentials as c
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = c.getEmailAddress()
EMAIL_PASSWORD = c.getPassword()

def alertMail():
    msg = EmailMessage()
    msg['Subject'] = 'SECURITY ALERT !!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'gargikulkarni1999@gmail.com'
    msg.set_content('An intruder is on your door')
    msg.add_attachment('images/capture.jpg')




    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:


        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)




        smtp.send_message(msg)


