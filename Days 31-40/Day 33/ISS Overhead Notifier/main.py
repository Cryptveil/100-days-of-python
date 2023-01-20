import requests
from datetime import datetime
import math
import smtplib

MY_LAT = -16.680519
MY_LONG = -49.256130
EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def iss_position():
    longitude_floor = math.floor(MY_LONG-5)
    longitude_ceiling = math.floor(MY_LONG+5)
    latitude_floor = math.floor(MY_LAT-5)
    latitude_ceiling = math.floor(MY_LAT+5)

    if iss_longitude in range(longitude_floor, longitude_ceiling):
        if iss_latitude in range(latitude_floor, latitude_ceiling):
            return True
    return False


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

if iss_position() and current_hour < sunrise or current_hour > sunset:
    with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Look up!")
