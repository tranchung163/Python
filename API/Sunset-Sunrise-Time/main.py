import requests
import smtplib
import datetime

MY_LATITUDE = 33.835293
MY_LONGTITUDE = -117.914505
MY_EMAIL = 'chungchuong163@gmail.com'
MY_PASSWORD = 'anhyeuem12'

def is_over_head():
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longtitude = float(data_iss["iss_position"]["longitude"])

    if MY_LATITUDE + 5 >= iss_latitude >= MY_LATITUDE - 5 and MY_LONGTITUDE + 5 >= iss_longtitude >= MY_LONGTITUDE -5:
        return True


def is_night_time():
    my_parameter = {
        "lat": MY_LATITUDE,
        "lng": float(MY_LONGTITUDE),
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=my_parameter)
    response.raise_for_status()
    data = response.json()
    sun_rise = int(data['results']['sunrise'].split('T')[1].split(":")[0]) 
    sun_set = int(data['results']['sunset'].split('T')[1].split(":")[0]) 

    time_now = datetime.datetime.now()
    if time_now >= sun_set or time_now <= sun_rise:
        return True

        
while True:
    if is_over_head() and is_night_time():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='tranchung163@gmail.com',
            msg="Subject: HE\n\n ISS is over your head"
        )

