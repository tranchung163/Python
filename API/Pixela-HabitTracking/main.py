import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

TOKEN = "thisisunknown"
USER_NAME = "tranchung163"

GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
POST_ENDPOINT = f"https://pixe.la/v1/users/{USER_NAME}/graphs/test-graph"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_configs = {
    "id": "test-graph",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu",
}


header = {
    "X-USER-TOKEN": TOKEN,
}


today = datetime.now().strftime("%Y%m%d")

post_params ={
    "date": today,
    "quantity": "5.7",
    
}

response = requests.post(url=POST_ENDPOINT, headers=header, json=post_params)
print(response.text)
