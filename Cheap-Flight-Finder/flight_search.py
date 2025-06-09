import requests
from exports import *
from datetime import datetime, timedelta
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iatf_code(self, city):
        query = {
            "term": city,
            "limit": 1,
            "location_types": "city"
        }
        response = requests.get(
            url=TEQUILA_LOCATIONS_ENDPOINT,
            params=query,
            headers=TEQUILA_HEADERS
            )
        response.raise_for_status()
        self.iatf_code = response.json()["locations"][0]["code"]
        return self.iatf_code

    def search_flights(self, destination):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (datetime.now() + timedelta(days=30*6)).strftime("%d/%m/%Y")
        query = {
            "fly_from": "LON",
            "fly_to": destination, 
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(
            TEQUILA_SEARCH_ENDPOINT, 
            params=query,
            headers=TEQUILA_HEADERS,
        )
        response.raise_for_status()
        data = response.json()["data"]
        if len(data) > 0:
            flight = data[0]
            price = flight["price"]
            origin_city = flight["cityFrom"]
            origin_airport = flight["flyFrom"]
            destination_city = flight["cityTo"]
            destination_airport = flight["flyTo"]
            out_date = flight["route"][0]["local_departure"].split("T")[0]
            return_date = flight["route"][1]["local_arrival"].split("T")[0]
            flight_data = FlightData(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)
            return flight_data
        else:
            print(f"No flights for {destination}")
        

