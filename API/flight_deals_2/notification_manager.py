from twilio.rest import Client
import os
import smtplib

TWILIO_SID = "AC4376f796864ec5682d81818f1c47ed90"
TWILIO_AUTH_TOKEN = "07f084166cc29578f76bab1b6563275b"
TWILIO_VIRTUAL_NUMBER = "+14242288723"
MY_NUMBER = "+17144586728"
MY_EMAIL = 'chungchuong163@gmail.com'
MY_PASSWORD = os.environ["MY_PASSWORD"]

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=MY_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        
    def send_emails(self, to_address, message):
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_address,
            msg=f"Subject: Flight Alert\n\n {message}",
        )
        