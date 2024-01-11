import easyimap as e
import credentials as c
import alexaa as al

def retirve_mail():
    password = c.getPassword()
    user = c.getEmailAddress()

    server = e.connect('imap.gmail.com', user , password)

    email = server.mail(server.listids()[0])

    #print(email.title)

    #print(email.from_addr)

    #print(email.body)

    if 'Allow' in email.body:
        al.talk("DOOR UNLOCKED")
        al.talk("WELCOME IN")
        print("ALLOWED")
    else:
        al.talk("SOORY ACCESS DENIED")
        print("ACCESS DENIED")
