#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pp, pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


flight_search = FlightSearch()
get_prices = FlightData()
sheety = DataManager()
notification = NotificationManager()

sheet_data = sheety.get_destination_data()


# for city in sheet_data: 
#     city_name = city['city']
#     iata_code = flight_search.get_iata_code(city_name)
#     update_to_sheet = sheety.update_destination_code(city['id'], iata_code)
for city in sheet_data:
    city_name = city['city']
    city_iata_code = flight_search.get_iata_code(city_name)
    prices = get_prices.get_departures_prices(city_iata_code)
    lowest_price = city['lowestPrice']
    if prices < lowest_price:
        notification.get_notifications(city_name, city_iata_code, prices)
        


    






