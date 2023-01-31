import requests
from bs4 import BeautifulSoup
import smtplib
import os

AMAZON_URL = "https://tinyurl.com/526but8b"
EMAIL = "hjgameplays@gmail.com"
GMAIL_TOKEN = os.environ["GMAIL_TOKEN"]
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
MSG = "Subject: Price drop!\n\nThe new price for the product is:"

headers = {
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
        }

response = requests.get(url=AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen")

# Since the price is in BRL, we need to change the "," to a "."
formatted_price = float(price.getText().replace(",", ".").split("R$")[1])

if formatted_price >= 400:
    with smtplib.SMTP(SMTP_SERVER, port=PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=GMAIL_TOKEN)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"{MSG} R${formatted_price:.2f}")
