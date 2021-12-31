import requests
SHEETY_API_ENDPOINT = "https://api.sheety.co/a5ef226282cad66b0d530bc4bfd36779/copyOfFlightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        self.destination_data = requests.get(SHEETY_API_ENDPOINT).json()['prices']
        return self.destination_data

    def update_destination_code(self, city_id, iata_code):
       
        new_data = {
            "price":{
                "iataCode": iata_code,
            }
        }
        code_address = f"{SHEETY_API_ENDPOINT}/{city_id}"
        response = requests.put(code_address, json=new_data)
        print(response.text)




        