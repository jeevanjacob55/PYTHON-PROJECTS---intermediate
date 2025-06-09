#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()


# data_manager.update_iatf()

sheety_data = data_manager.sheety_data
for destination in sheety_data:
    destination_code = destination["iataCode"]
    lowest_price = destination["lowestPrice"]
    flight_data = flight_search.search_flights(destination_code)
    try:
        if flight_data.price <= lowest_price:
            notification_manager = NotificationManager(flight_data)
            notification_manager.send_message()
    except AttributeError:
        pass
    
