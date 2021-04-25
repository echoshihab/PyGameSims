from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt
import os

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# apis

# SHEETY
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN =  os.environ.get("SHEETY_TOKEN")
SHEETY_HEADER = {
    "Authorization": F"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

# KIWI
KIWI_KEY = os.environ.get("KIWI_KEY")
KIWI_LOC_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_HEADER = {
    "accept": "application/json",
    "apikey": f"{KIWI_KEY}"
}

KIWI_PARAMS_LOC = {
    "term": "",
    "locale": "en-US",
    "location_types": "airport",
    "limit": 10,
    "active_only": True
}

#twillio
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_FROM")
TWILIO_TO = os.environ.get("TWILIO_TO")
# ============This will update google sheet with IATA code if does not exist=========================

data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_TOKEN, SHEETY_HEADER)
sheety_data = data_manager.get_sheet_data()

flight_search = FlightSearch(loc_endpoint=KIWI_LOC_ENDPOINT, flight_endpoint=KIWI_FLIGHT_ENDPOINT, key=KIWI_KEY, header=KIWI_HEADER)
notification_manager = NotificationManager(sid=TWILIO_SID, token=TWILIO_TOKEN)


for item in sheety_data["prices"]:
    if len(item["iataCode"]) < 1:
        iata_code = flight_search.get_IATA_code()
        update_data = {
                "price": {
                    "iataCode": iata_code
                }
            }
        update_sheet_response = data_manager.update_sheet_data(row=item["id"], body=update_data)



# ===================Search for Cheapest flights ======#
tomorrow = (dt.datetime.now() + dt.timedelta(days=1))
return_start = tomorrow + dt.timedelta(days=7)
six_month_later = tomorrow + dt.timedelta(days=180)

KIWI_PARAMS_FLIGHT = {
    "fly_from": "LON",
    "fly_to": "",
    "curr": "GBP",
    "dateFrom": tomorrow.strftime("%d/%m/%Y"),
    "dateTo": six_month_later.strftime("%d/%m/%Y"),
    "nights_in_dst_from": 5,
    "nights_in_dst_to": 7,
    "price_to": "",
    "max_stopovers": 0,
    "limit": 1
}

#notify user by msg
for item in sheety_data["prices"]:
    KIWI_PARAMS_FLIGHT["fly_to"] = item["iataCode"]
    KIWI_PARAMS_FLIGHT["price_to"] = item["lowestPrice"]
    kiwi_data = flight_search.get_cheapest_flight(params=KIWI_PARAMS_FLIGHT)
    flight_data = FlightData(kiwi_data, from_city="London", from_code="LCY")
    formatted_msg = flight_data.get_formatted_data(to_city=item["city"], to_city_code=item["iataCode"])
    if formatted_msg is not None:
        msg_id = notification_manager.send_msg(from_num=TWILIO_FROM, to_num=TWILIO_TO, msg=formatted_msg)
        print(msg_id)

