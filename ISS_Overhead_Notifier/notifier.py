import requests
import datetime as dt

MY_LAT = 43.256531
MY_LONG = -79.874420

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
time_now = dt.datetime.now()