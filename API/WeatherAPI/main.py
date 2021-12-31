import requests
from twilio.rest import Client
import os

API_KEY = "cf3ba2e54ffbc400db7978d57b177896"
MY_LAT = 34.052235
MY_LONG = -118.243683
EXCLUDE = "current,minutely,daily"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'AC4376f796864ec5682d81818f1c47ed90'
auth_token = '07f084166cc29578f76bab1b6563275b'
client = Client(account_sid, auth_token)


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": EXCLUDE,
    "appid": API_KEY
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
# print(weather_data)

# weather_id = [weather_data[i]['weather'][0]['id'] for i in range(0,12)]

will_rain = False
weather_slice = weather_data[:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages \
                .create(
                     body="It is going to rain today. You should bring an umbrella.",
                     from_='+14242288723',
                     to='+17144586728'
                 )



