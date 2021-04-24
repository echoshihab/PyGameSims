import requests
import datetime as dt
import os

# USE natural language processing API from Nutritionix to store exercise data in Google Sheets (using Sheety API)

# user details
DOB = dt.datetime(year=1985, month=4, day=5)
now = dt.datetime.now()
HEIGHT = 170.68
WEIGHT = 70.31
age = now.year - DOB.year - ((now.month, now.day) < (DOB.month, DOB.day))
GENDER = "male"

# nutritionix api
NIX_API_ID = os.environ["NIX_API_ID"]
NIX_API_KEY = os.environ["NIX_API_KEY"]
NIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# sheety
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]

sheety_header = {
    "authorization": f"Bearer {SHEETY_AUTH}"
}

user_input = input("What did you do today?: ")

header = {
    "x-app-id": NIX_API_ID,
    "x-app-key": NIX_API_KEY,
    "Content-Type": "application/json"
}

request_body = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": age

}

response_nix = requests.post(url=NIX_API_ENDPOINT, json=request_body, headers=header)
json_data = response_nix.json()

exercise_date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for item in json_data['exercises']:
    sheety_body = {
        "workout":
            {
                "date": exercise_date,
                "time": time,
                "exercise": item['name'],
                "duration": item['duration_min'],
                "calories": item['nf_calories']
            }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_header)
    print(sheety_response.json())
