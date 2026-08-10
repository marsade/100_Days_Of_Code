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
        res = requests.get(self.sheety_url, headers=self.headers)
        return(res.json()["prices"])

    def update_lowest_price(self, row_id, new_price):
        self.put_url = f"{self.sheety_url}/{row_id}"

        payload = {
            "price": {
                "lowestPrice": new_price
            }
        }
        res = requests.put(self.put_url, headers=self.headers, json=payload)
        return (res.json())