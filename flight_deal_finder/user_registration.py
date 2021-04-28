import requests
from main import SHEETY_USERS_ENDPOINT, SHEETY_TOKEN

SHEETY_HEADER = {
    "Authorization": F"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

print("Welcome to Shihab's flight club")
print("We find the best flight deals and email you")


repeat = True
valid = False

while repeat:
    first_name = input("What is your first name? ").title()
    last_name = input("What is your last name? ").title()
    email = input("What is your email? ").lower()
    confirm_email = input("Type your email again?").lower()

    if email != confirm_email:
        print("Email & Confirmed Email do not match!")
        response = input("Type Y to start over or N to exit").lower()
        repeat = True if response == 'y' else False
    else:
        repeat = False
        valid = True
        print("You are in the club!")

if valid:
    user_data = {
        "user":
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
    }
    sheety_response = requests.post(url=SHEETY_USERS_ENDPOINT, json=user_data, headers=SHEETY_HEADER)
    print(sheety_response.json())







