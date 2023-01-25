import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
GENDER = "male"
WEIGHT = 63.5
HEIGHT = 180
AGE = 25

exercise_headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "x-remote-user-id": "0",
        }

exercise_parameters = {
        "query": input("Tell me which exercises you did: "),
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
        }

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_response = requests.post(
                        url=exercise_endpoint,
                        headers=exercise_headers,
                        json=exercise_parameters
                        )
exercise_result = exercise_response.json()["exercises"]

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M:%S")

sheety_endpoint = os.environ["SHEET_ENDPOINT"]

sheety_headers = {
        "Authorization": f"Bearer {os.environ['TOKEN']}"
        }

for index, exercise in enumerate(exercise_result):
    name = exercise_result[index]["name"].capitalize()
    duration = exercise_result[index]["duration_min"]
    calories = exercise_result[index]["nf_calories"]
    sheety_params = {
            "workout": {
                "date": today,
                "time": time,
                "exercise": name,
                "duration": duration,
                "calories": calories,
                }
            }
    print()
    sheety_response = requests.post(
                                    url=sheety_endpoint,
                                    json=sheety_params,
                                    headers=sheety_headers
                                    )
    print(sheety_response.text)
