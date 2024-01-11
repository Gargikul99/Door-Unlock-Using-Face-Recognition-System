from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def my_msg():
    account_sid = '<account_sid>'
    auth_token = '<auth_token>'
    client = Client(account_sid, auth_token)

    from_whatsapp_number='whatsapp:+<number here>'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+<number>'


    client.messages.create(body='intruder....!!!!',
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
