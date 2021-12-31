from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a5ef226282cad66b0d530bc4bfd36779/copyOfFlightDeals/prices"
USERS_ENDPOINT = "https://api.sheety.co/a5ef226282cad66b0d530bc4bfd36779/copyOfFlightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.emails_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
    def get_emails_data(self):
        response = requests.get(url=USERS_ENDPOINT).json()
        self.emails_data = response["users"]
        return self.emails_data