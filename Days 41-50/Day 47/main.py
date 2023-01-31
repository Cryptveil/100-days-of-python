import requests
from bs4 import BeautifulSoup
import smtplib
import os

AMAZON_URL = "https://tinyurl.com/526but8b"
GMAIL_TOKEN = os.environ["GMAIL_TOKEN"]

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

