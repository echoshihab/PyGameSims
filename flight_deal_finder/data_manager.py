import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint, token, header):
        self.endpoint = endpoint
        self.token = token
        self.header = header

    def get_sheet_data(self):
        sheety_response = requests.get(url=self.endpoint, headers=self.header)
        sheety_response.raise_for_status()
        return sheety_response.json()

    def update_sheet_data(self, row, body):
        update_sheety_response = requests.put(url=f'{self.endpoint}/{row}', json=body, headers=self.header)
        return update_sheety_response.json()