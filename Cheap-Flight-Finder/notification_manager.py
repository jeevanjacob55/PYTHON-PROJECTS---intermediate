from exports import *
from twilio.rest import Client
from flight_data import FlightData

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data: FlightData):
        self.price = flight_data.price
        self.origin_city = flight_data.origin_city
        self.origin_airport = flight_data.origin_airport
        self.destination_city = flight_data.destination_city
        self.destination_airport = flight_data.destination_airport
        self.out_date = flight_data.out_date
        self.return_date = flight_data.return_date

    def send_message(self):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        body = f"Low price alert! Only £{self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport} from {self.out_date} to {self.return_date}"
        message = client.messages \
            .create(
                    body=body,
                    from_=TWILIO_NUMBER,
                    to=DESTINATION_NUMBER,
                )
        print(message)
        print(message.status)