import json
import requests
from exports import *
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint

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
            "one_for_city": 0,
            "max_stopovers": 0,
        }
        response = requests.get(
            TEQUILA_SEARCH_ENDPOINT, 
            params=query,
            headers=TEQUILA_HEADERS)
        response.raise_for_status()
        if len(response.json()["data"]) > 0:
            data = response.json()["data"][0]
            flight_data = FlightData(
                data["price"], 
                data["cityFrom"], 
                data["flyFrom"], 
                data["cityTo"], 
                data["flyTo"], 
                data["route"][0]["local_departure"].split("T")[0], 
                data["route"][1]["local_departure"].split("T")[0])
            return flight_data
        else:
            query["max_stopovers"] = 1
            response = requests.get(
                TEQUILA_SEARCH_ENDPOINT, 
                params=query,
                headers=TEQUILA_HEADERS)
            response.raise_for_status()
            if len(response.json()["data"]) > 0:
                data = response.json()["data"][0]
                flight_data = FlightData(
                    data["price"], 
                    data["cityFrom"], 
                    data["flyFrom"], 
                    data["cityTo"], 
                    data["flyTo"], 
                    data["route"][0]["local_departure"].split("T")[0], 
                    data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"])
                return flight_data
            else:
                print(f"No flights to {destination}.")
                return None