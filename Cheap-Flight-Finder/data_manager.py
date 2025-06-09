import requests
from exports import *
from flight_search import FlightSearch


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_data = self.get_sheety_data()

    def get_sheety_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        response.raise_for_status()
        self.sheety_data = response.json()["prices"]
        return self.sheety_data

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
                f"{SHEETY_ENDPOINT}/{id}",
                json=new_data, 
                headers=SHEETY_HEADERS
            )
            response.raise_for_status()


