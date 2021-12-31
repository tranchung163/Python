import requests

API_QUESTION = 'https://opentdb.com/api.php'
parameter = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get(API_QUESTION, params=parameter)
response.raise_for_status()
question_data = response.json()["results"]
