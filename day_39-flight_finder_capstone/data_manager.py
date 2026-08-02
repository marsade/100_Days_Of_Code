#!/usr/bin/env python3
import os
import requests
from dotenv import load_dotenv


load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = os.getenv("SHEET_URL")
        self.headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_TOKEN")}"
        }

    def get_prices(self):
        self.res = requests.get(self.sheety_url, headers=self.headers)
        return(self.res.json()["prices"])
