import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -16.680519
MY_LONG = -49.256130
EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
PORT = 587


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    check_1 = MY_LAT-5 <= iss_latitude <= MY_LAT+5
    check_2 = MY_LONG-5 <= iss_longitude <= MY_LONG+5

    if check_1 and check_2:
        return True


def is_night_time():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
            "https://api.sunrise-sunset.org/json",
            params=parameters,
            )

    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night_time() and iss_position():
        with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg="Subject: Look up!\n\nThe ISS is above you in the sky."
                                )
