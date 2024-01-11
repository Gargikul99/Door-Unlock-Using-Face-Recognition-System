from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def my_msg():
    account_sid = 'AC47fba6c272aa3ba38cf148984c92996a'
    auth_token = '9d8021f72af32c59839f08fc67d44283'
    client = Client(account_sid, auth_token)

    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+917057622382'


    client.messages.create(body='intruder....!!!!',
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
