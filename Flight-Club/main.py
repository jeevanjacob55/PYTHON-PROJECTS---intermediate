from exports import *

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()


## get flights 
def notify_flight_deals():
    sheety_data_prices = data_manager.sheety_data_prices
    for destination in sheety_data_prices:
        destination_code = destination["iataCode"]
        lowest_price = destination["lowestPrice"]
        flight_data = flight_search.search_flights(destination_code)
        try:
            if flight_data.price <= lowest_price:
                notification_manager = NotificationManager(flight_data)
                notification_manager.send_message()
                notification_manager.send_email()
        except AttributeError:
            pass

def add_user():
    print("Welcome to Flight Club.")
    print("We find the best flight deals and email you.")

    first_name = input("What is your first name?\n").title()
    last_name = input("What is your last name?\n").title()
    email = input("What is your email?\n")
    email2 = input("Type your email again.\n")
    if email == email2:
        data_manager.add_user(first_name, last_name, email)
        print("You are in the club!")

if __name__ == "__main__":
    # data_manager.update_iatf()
    add_user()
    notify_flight_deals()
    