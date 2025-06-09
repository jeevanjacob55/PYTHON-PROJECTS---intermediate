import requests
from exports import *
from flight_search import FlightSearch


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_data_prices = self.get_sheety_data_prices()
        self.sheety_data_users = self.get_sheety_data_users()

    def get_sheety_data_prices(self):
        response = requests.get(SHEETY_ENDPOINT_PRICES, headers=SHEETY_HEADERS)
        response.raise_for_status()
        self.sheety_data_prices = response.json()["prices"]
        return self.sheety_data_prices

    def get_sheety_data_users(self):
        response = requests.get(SHEETY_ENDPOINT_USERS, headers=SHEETY_HEADERS)
        response.raise_for_status()
        self.sheety_data_users = response.json()["users"]
        return self.sheety_data_users

    def update_iatf(self):
        for destination in self.sheety_data:
            id = destination["id"]
            city = destination["city"]
            iata_code = FlightSearch().get_iatf_code(city)
            new_data = {
                "price": {
                    "iataCode": iata_code,
                }
            }
            response = requests.put(
                f"{SHEETY_ENDPOINT_PRICES}/{id}",
                json=new_data, 
                headers=SHEETY_HEADERS
            )
            response.raise_for_status()

    def add_user(self, first_name, last_name, email):
            new_data = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                }
            }
            response = requests.post(
                f"{SHEETY_ENDPOINT_USERS}",
                json=new_data, 
                headers=SHEETY_HEADERS
            )
            response.raise_for_status()



