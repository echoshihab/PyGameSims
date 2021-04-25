import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, loc_endpoint, flight_endpoint, key, header):
        self.loc_endpoint = loc_endpoint
        self.flight_endpoint = flight_endpoint
        self.key = key
        self.header = header

    def get_IATA_code(self, params):
        iata_response = requests.get(url=self.loc_endpoint, params=params, headers=self.header)
        iata_data = iata_response.json()
        if len(iata_data["locations"]) > 1:
            iata_code = iata_data["locations"][0]["city"]["code"]
        else:
            iata_code = iata_data["locations"][0]["code"]
        return iata_code

    def get_cheapest_flight(self, params):
        cheap_flight_data = requests.get(url=self.flight_endpoint, params=params, headers=self.header)
        return cheap_flight_data.json()
