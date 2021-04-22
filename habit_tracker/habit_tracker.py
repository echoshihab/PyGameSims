import requests
import datetime as dt

USERNAME = "yourusername"
TOKEN = "yourtoken"

date_today = dt.datetime.today().strftime("%Y%m%d")
pixela_endppoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}

# create user


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endppoint, json=user_params)
print(response.text)

# Create a graph

graph_params = {
    "id": "yourgraphid",
    "name": "yourgraphname",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

graph_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs"

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# post a pixel

pixel_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs/yourgraphname"

pixel_params = {
    "date": date_today,
    "quantity": "2"
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# update a pixel
update_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs/yourgraphname/{date_today}"

update_params = {
    "quantity": "3.5"
}

response = requests.put(url=update_endpoint, json=update_params, headers=headers)

print(response.text)

# delete a pixel


delete_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs/yourgraphname/{date_today}"

response = requests.delete(url=delete_endpoint, headers=headers)

print(response.text)
