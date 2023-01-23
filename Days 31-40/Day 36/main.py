import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# Free API key so doesn't matter if it goes public, have fun!
ALPHA_API = "WPH2B0O2G81ANNKY"

alpha_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": ALPHA_API,
        }

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").
results = requests.get(
        "https://www.alphavantage.co/query",
        params=alpha_params,
        )
alpha_data = results.json()["Time Series (Daily)"]
data_list = [value for (key, value) in alpha_data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_closing_price = float(data_list[1]["4. close"])

difference = abs(yesterday_closing_price - day_before_closing_price)
difference_percentage = (difference*100)/yesterday_closing_price

if difference_percentage >= 5:
    print("Get News")
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for
# the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title
# and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings show
the funds' and investors' portfolio positions as of March 31st, near the
height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings show
the funds' and investors' portfolio positions as of March 31st, near the
height of the coronavirus market crash.
"""
