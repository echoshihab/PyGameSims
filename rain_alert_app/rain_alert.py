import requests
import os
from twilio.rest import Client

# openweathermap set up
api_key = "c6baf013df628b677e9fc43e87579a44"
lat = "43.25"
lon = "-79.87"

api_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=api_params)
response.raise_for_status()
data_twelve_hour = response.json()["hourly"][:12]

bring_umbrella = False
weather_list = []

for index in range(len(data_twelve_hour)):
    # less than 700 indicates rain or snow
    if data_twelve_hour[index]["weather"][0]["id"] < 700:
        bring_umbrella = True
        weather_list.append(data_twelve_hour[index]["weather"][0]["main"])

weather_list = set(weather_list)
print(weather_list)

try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
except KeyError:
    print("Error Authenticating to Twilio API")


if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"for next 12 hours Hamilton has possibility of {','.join(weather_list)}, Bring an umbrella ☂️: Shihab's Weather App 😊",
        from_='twilio number',
        to='verified number'
    )

    print(message.sid)
