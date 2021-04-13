import requests
from datetime import datetime
import threading
import smtplib

MY_LAT = 43.256531
MY_LONG = -79.874420


# Your position is within +5 or -5 degrees of the ISS position.
def is_ISS_nearby():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    main_data = iss_response.json()

    iss_latitude = float(main_data["iss_position"]["latitude"])
    iss_longitude = float(main_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 \
            and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def is_dark():
    time_now = datetime.now()
    current_hour = time_now.hour
    if sunset < current_hour < sunrise and is_ISS_nearby():
        return True
    return False


def send_mail():
    my_email = "fake@email.com"
    password = "fakepassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="test@test.com",
                            msg=f"Subject:Look Up Now!\n\nLook up for ISS")


def main_notify():
    #reference - Alex Martelli's answer from https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
    threading.Timer(60.0, main_notify).start()
    if is_dark() and is_ISS_nearby():
        send_mail()


main_notify()
