import smtplib
import datetime as dt
import random

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()

MSG = f"Subject: Quote of the day\n\n{random.choice(quotes)}"
EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
RECIPIENT = ""

now = dt.datetime.now()
today = now.weekday()
if today == 3:
    with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=RECIPIENT, msg=MSG)
