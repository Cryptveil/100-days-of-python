import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# Free API keys so doesn't matter if it goes public, have fun!
ALPHA_API = "WPH2B0O2G81ANNKY"
NEWS_API = "965c78ee57b540dfaa818c267bc796ae"

TWILIO_SID = ""
TWILIO_AUTH = ""

alpha_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": ALPHA_API,
        }

alpha_results = requests.get(
        "https://www.alphavantage.co/query",
        params=alpha_params,
        )
alpha_data = alpha_results.json()["Time Series (Daily)"]
data_list = [value for (key, value) in alpha_data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_closing_price = float(data_list[1]["4. close"])

difference = abs(yesterday_closing_price - day_before_closing_price)
difference_percentage = (difference*100)/yesterday_closing_price

if difference_percentage >= 4:
    news_params = {
            "qInTitle": "Tesla",
            "apiKey": NEWS_API,
            }

    news_results = requests.get(
            "https://newsapi.org/v2/everything",
            params=news_params,
            )

    news_data = news_results.json()["articles"]
    three_articles = news_data[:3]
    news = [f"Headline: {news_data['title']}.\n"
            f"Brief: {news_data['description']}" for news_data in
            three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in news:
        message = client.messages.create(
                body=article,
                from_="",
                to=""
                )
