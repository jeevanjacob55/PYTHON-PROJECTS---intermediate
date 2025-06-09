from exports import *
from twilio.rest import Client
from flight_data import FlightData
from data_manager import DataManager
import smtplib

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
        self.stop_overs = flight_data.stop_overs, 
        self.via_city = flight_data.via_city

        if self.stop_overs[0] == 0:
            self.body = f"Subject:Low price alert!\n\nOnly £{self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport} from {self.out_date} to {self.return_date}"
        else:
            self.body = f"Subject:Low price alert!\n\nOnly £{self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport} from {self.out_date} to {self.return_date}\nFlight has {self.stop_overs} stop over, via {self.via_city}"


    def send_message(self):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
                    body=self.body,
                    from_=TWILIO_NUMBER,
                    to=DESTINATION_NUMBER,
                )
        print(message.body)

    def send_emails(self):
        emails = [user["email"] for user in DataManager().sheety_data_users]
        for to_email in emails:
            print(to_email)
            with smtplib.SMTP(SMTP) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
                connection.sendemail(
                    from_addr=MY_EMAIL, 
                    to_addrs=to_email, 
                    msg=self.body
                )
