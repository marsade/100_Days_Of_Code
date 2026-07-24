#!/usr/bin/env python3
import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
percent = 0

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("STOCK_API")
}

parameters_news = {
    "q": COMPANY_NAME,
    "searchIn": "content",
    "apiKey": os.getenv("NEWS_APIKEY")
}

def send_sms(msg_body):
    account_sid = os.getenv("TW_ACC_SID")
    auth_token = os.getenv("TW_AUTH")
    client = Client(account_sid, auth_token)
    for msg in msg_body:
        msg_text = f"{STOCK}: {"🔺" if percent > 0 else "🔻"}{abs(percent)}%\nHeadline: {msg[0]}\nBrief: {msg[1]}"
        msg_text_trunc = (msg_text[:157] +  "...") if len(msg_text) > 160 else msg_text
        message = client.messages \
            .create(
                body=msg_text_trunc,
                from_="+19382536462",
                to="+2349118436707"
            )
        print(message.status)

def get_news():
    news_res = requests.get(NEWS_ENDPOINT, params=parameters_news)
    news_res.raise_for_status()
    first_three_art = news_res.json()["articles"][:2]
    msg_content = [(art["title"], art["description"]) for art in first_three_art]
    send_sms(msg_content)


def get_stock():
    global percent
    stock_res = requests.get(STOCK_ENDPOINT, params=parameters_stock)
    stock_res.raise_for_status()
    daily_series = stock_res.json()["Time Series (Daily)"]
    first_two_dates = dict(list(daily_series.items())[:2])

    entries = list(first_two_dates.items())

    first_close = float(entries[0][1]["4. close"])
    second_close = float(entries[1][1]["4. close"])

    percent_fl = ((first_close - second_close)/first_close) * 100
    percent = int(percent_fl)
    if percent <= -5 or percent >= 5:
        get_news()

get_stock()
