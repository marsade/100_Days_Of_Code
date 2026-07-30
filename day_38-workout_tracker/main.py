#!/usr/bin/env python3
'''Workout Tracker'''
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NUTRI_API_KEY")
APP_ID = os.getenv("NUTRI_APP_ID")


nutri_url = "https://app.100daysofpython.dev"
sheety_url = os.getenv("SHEET_URL")

headers_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
headers_sheety = {
    "Authorization": f"Basic {os.getenv("TOKEN")}"
}
ans  =  input("Tell me which exercises you did: ")
ans_split = ans.split("and")

now = datetime.now()

for i in range(len(ans_split)):
    ex_config = {
        "query": ans_split[i]
    }

    ex_endpoint = f"{nutri_url}/v1/nutrition/natural/exercise"
    nutri_res = requests.post(url=ex_endpoint, json=ex_config, headers=headers_nutri)
    data = nutri_res.json()
    data = data["exercises"][0]

    sheets_config = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%I:%M %p"),
            "exercise": data["name"].capitalize(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    sheety_res = requests.post(url=sheety_url, json=sheets_config, headers=headers_sheety)
