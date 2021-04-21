import requests
import datetime as dt
import os
from twilio.rest import Client

today = dt.datetime.now()
yesterday = dt.datetime.strftime(today - dt.timedelta(1), '%Y-%m-%d')
day_before_yesterday = dt.datetime.strftime(today - dt.timedelta(2), '%Y-%m-%d')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

try:
    api_key_stock = os.environ['ALPHA_STOCK_KEY']
except KeyError:
    print("Error Authenticating to Alpha Advantage Stock API")

stock_endpoint = "https://www.alphavantage.co/query"

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock
}

stock_response = requests.get(stock_endpoint, params=stock_api_params)
stock_response.raise_for_status()

stock_data = stock_response.json()
yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
day_before_yesterday_close = float(stock_data['Time Series (Daily)'][day_before_yesterday]['4. close'])

percentage_change = ((yesterday_close - day_before_yesterday_close) * 100) / day_before_yesterday_close
percentage_change_formatted = float("{:.2f}".format(abs(percentage_change)))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
try:
    api_key_news = os.environ['NEWS_API_KEY']
except KeyError:
    print("Error Authenticating to Alpha Advantage Stock API")

news_endpoint = 'https://newsapi.org/v2/top-headlines'

news_api_params = {
    'q': COMPANY_NAME,
    'pageSize': 3,
    'page': 1,
    'apiKey': api_key_news
}

news_response = requests.get(news_endpoint, params=news_api_params)
news_data = news_response.json()
articles = news_data["articles"]
all_text = ''
for article in articles:
    all_text += 'Headline: ' + article['title'] + '\n'
    all_text += 'Brief: ' + article['description'] + '\n'

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
except KeyError:
    print("Error Authenticating to Twilio API")

# Optional: Format the SMS message like this:
indicator = '🔺' if percentage_change > 0 else '🔻'

if percentage_change > 5:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{COMPANY_NAME}: {indicator}{percentage_change_formatted}%\n{all_text}",
        from_='',  # TWILIO NUMBER
        to=''  # VERIFIED NUMBER
    )

    print(message.sid)
