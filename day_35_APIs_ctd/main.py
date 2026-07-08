#!/usr/bin/env python3
import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("TW_ACC_SID")
auth_token = os.environ.get("TW_AUTH")
paraneters = {
    "lat": 6.439415,  # 35.192595
    "lon": 3.469655, #33.374848
    "appid": os.environ.get("OWM_API_KEY"),
    "units": "metric",
    "cnt": 4
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=paraneters)
response.raise_for_status()
weather_data =  response.json()["list"]
weather_list = []

for hour in weather_data:
    weather_list.append(hour["weather"])
weather_ids = [info["id"] for info_item in weather_list for info in info_item]

print(weather_ids)
if any(id < 700 for id in weather_ids):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain, carry an ☂️",
            from_="+12299205434",
            to="+2349118436707"
        )
    print(message.status)