import requests
import datetime
from requests.auth import HTTPBasicAuth
import os

print(os.getenv("APP_ID"))
APP_ID = os.environ["APP_ID"]
APP_KEYS = os.environ["APP_KEYS"]


NUTRITION_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_API_ENDPOINT = os.environ["SHEET_API_ENDPOINT"]
USER_ID = os.environ["USER_ID"]
USER_PASS = os.environ["USER_PASS"]

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEYS,
}
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%I:%M %p")
exercise_text = input("what exercise you did: ")

nutrition_request = {
  "query": exercise_text,
  "gender": "male",
  "weight_kg": 69,
  "height_cm": 170,
  "age": 23,

}


nutrition_response = requests.post(url=NUTRITION_API_ENDPOINT, headers=HEADERS, json=nutrition_request) 
exercises_detail = nutrition_response.json()['exercises'] 
for exercises in exercises_detail:
    exercises_name = exercises['user_input']
    duration = exercises['duration_min']
    calories = exercises['nf_calories']
    
    sheet_input = {

        "working": {
            "date": today_date,
            "time": now_time,
            "exercise": exercises_name.title(),
            "duration": duration,
            "calories": calories,
        }
    }

    sheet_respone = requests.post(
        url=SHEET_API_ENDPOINT, 
        json=sheet_input,
        auth= (
            USER_ID,
            USER_PASS,
        )
        )

    print(sheet_respone.json())
