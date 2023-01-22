import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def stock_percent_change():
    av_endpoint = "https://www.alphavantage.co/query"
    av_api_key = os.environ.get("AV_API_KEY")
    av_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": av_api_key
    }
    av_response = requests.get(url=av_endpoint, params=av_parameters)
    av_response.raise_for_status()
    stock_data = av_response.json()

    yest = datetime.now() - timedelta(1)
    day_before = datetime.now() - timedelta(2)
    yesterday = datetime.strftime(yest, "%Y-%m-%d")
    day_before_yesterday = datetime.strftime(day_before, "%Y-%m-%d")

    yesterday_data = stock_data["Time Series (Daily)"][yesterday]
    yesterday_close_price = float(yesterday_data["4. close"])
    day_before_yesterday_data = stock_data["Time Series (Daily)"][day_before_yesterday]
    day_before_yesterday_close_price = float(day_before_yesterday_data["4. close"])

    percent_change = (yesterday_close_price - day_before_yesterday_close_price) / day_before_yesterday_close_price * 100

    return percent_change

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news():
    news_endpoint = "https://newsapi.org/v2/everything"
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_parameters = {
        'q': COMPANY_NAME,
        'apikey': news_api_key
    }
    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    news_articles = news_data["articles"]
    first_three_articles = news_articles[:3]
    return first_three_articles


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_messages(messages, percent_change):
    twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(twilio_account_sid, twilio_auth_token)
    up_down = "🔺" if percent_change > 0 else "🔻"

    for msg in messages:
        message = client.messages \
            .create(
                body=f"{STOCK}: {up_down}{percent_change}% \nHeadline: {msg['title']}\nBrief: {msg['description']}",
                from_='+19047805729',
                to='+15054928001'
            )
        print(message.status)


if abs(stock_percent_change()) > 4:
    news = get_news()
    percent_ch = round(stock_percent_change(), 2)
    send_messages(news, percent_ch)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
