import requests
from data_manager import DataManager
from datetime import datetime, timedelta

API_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "pVPGvUfXPEMNNoTKb2DG_S8EYSDeXwQq"
NOW_TIME = datetime.now().strftime("%d/%m/%Y")
SIX_MONTHS_FROM_NOW = (datetime.now() + timedelta(days=30*6)).strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    def get_departures_prices(self, iata_code):
        header = {
            "apikey": API_KEY,
        }

        flight_para = {
            "fly_from": "LAX",
            "fly_to": iata_code,
            "date_from": NOW_TIME,
            "date_to": SIX_MONTHS_FROM_NOW,
            "curr": "USD",
        }

        self.prices_return = requests.get(url=API_SEARCH_ENDPOINT, headers=header, params=flight_para).json()['data'][0]['price']
        return self.prices_return



