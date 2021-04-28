import requests

class FlightData:
    def __init__(self, data, from_city, from_code):
        self.data = data
        self.from_city = from_city
        self.from_code = from_code
    def get_formatted_data(self, to_city, to_city_code):
        if len(self.data["data"]) > 0:
            from_date = (self.data["data"][0]['route'][0]['local_departure']).split('T')[0]
            to_date = (self.data["data"][0]['route'][1]['local_departure']).split('T')[0]
            sms_msg = f"Low price alert! Only £{self.data['data'][0]['price']} to fly from " \
                      f"{self.from_city}-{self.from_code} to {to_city}-{to_city_code} from {from_date} to {to_date} \n"\
                      f"https://www.google.co.uk/flights?hl=en#flt={self.from_code}.{to_city_code}.{from_date}*{to_city_code}.{self.from_code}.{to_date}"
            return sms_msg
        else:
            return None


