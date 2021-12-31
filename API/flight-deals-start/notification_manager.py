import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

class NotificationManager:
    def __init__(self):
        pass

    def get_notifications(self,city_name, city_iata_code, price):
        message = client.messages \
                .create(
                     body=f"\n\n   LOW PRICE ALERT: Only {price} USD To fly from Los Angeles - LAX to {city_name} - {city_iata_code}  ",
                     from_='+14242288723',
                     to='+17144586728'
                )
        return message