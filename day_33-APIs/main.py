#!/usr/bin/env python3
from datetime import datetime
import requests

MY_LAT = 35.196880
MY_LNG = 33.368225

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "Asia/Nicosia"
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]


print(sunset)