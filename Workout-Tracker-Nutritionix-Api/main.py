import requests
import os
from datetime import datetime

# nutritionix
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
APP_KEY = os.environ.get("NUTRITIONIX_API_KEY")
URL = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{URL}/v2/natural/exercise"

# sheety
SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_ID}/workoutTracking/workouts"
SHEETY_AUTHORIZATION = os.environ.get("SHEETY_AUTHORIZATION")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

headers_sheety = {
    "authorization": f"Basic {SHEETY_AUTHORIZATION}",
}


params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 52.5,
    "height_cm": 150,
    "age": 27,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
data = response.json()["exercises"]

for exercise in data:
    exercise_info = {
        "workout": {
            "date": datetime.now().strftime("%d/%m%Y"),
            "time": datetime.now().time().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    print(exercise_info)

    response = requests.post(url=SHEETY_ENDPOINT, json=exercise_info, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
    response.raise_for_status()
    print(response)




