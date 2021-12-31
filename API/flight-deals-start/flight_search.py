import requests
from data_manager import DataManager
SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
API_KEY = "pVPGvUfXPEMNNoTKb2DG_S8EYSDeXwQq"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iata_code(self, city_name):    
        flight_para = {
            "term": city_name,
            "location_types": "city",
            "limit": 10,
            "locale": "en-US",
            "active_only": True,
            
            
        }
        header = {
            "apikey": API_KEY,
        }
        self.search_response = requests.get(SEARCH_API_ENDPOINT, params=flight_para, headers=header)
        return self.search_response.json()['locations'][0]['code']
        
    def get_destination_price(self, city_name):
        code = "TESTING"
        return code

