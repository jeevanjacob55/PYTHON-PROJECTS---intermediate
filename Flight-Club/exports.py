import os

SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_ENDPOINT_PRICES = f"https://api.sheety.co/{SHEETY_ID}/flightDeals/prices"
SHEETY_ENDPOINT_USERS = f"https://api.sheety.co/{SHEETY_ID}/flightDeals/users"
SHEETY_AUTHORIZATION = os.environ.get("SHEETY_AUTHORIZATION")
SHEETY_HEADERS = {
    "authorization" : f"Basic {SHEETY_AUTHORIZATION}"
}

TEQUILA_SERVER = "https://tequila-api.kiwi.com"
TEQUILA_LOCATIONS_ENDPOINT= f"{TEQUILA_SERVER}/locations/query"
TEQUILA_SEARCH_ENDPOINT= f"{TEQUILA_SERVER}/v2/search"
TEQUILA_API_KEY=os.environ.get("TEQUILA_API_KEY")
TEQUILA_HEADERS = {
    "apikey": TEQUILA_API_KEY,
}

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
DESTINATION_NUMBER = os.environ.get("DESTINATION_NUMBER")

MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP = os.environ.get("SMTP")