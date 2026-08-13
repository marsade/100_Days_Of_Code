#!/usr/bin/env python3
import os
import requests
from dotenv import load_dotenv


load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_price_url = os.getenv("SHEETY_PRICE_URL")
        self.sheety_users_url = os.getenv("SHEETY_USERS_URL")
        self.headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_TOKEN")}"
        }

    def get_prices(self):
        res = requests.get(self.sheety_price_url, headers=self.headers)
        return(res.json()["prices"])

    def get_customer_email(self):
        res = requests.get(self.sheety_users_url, headers=self.headers)
        return(res.json()["users"])

    def update_lowest_price(self, row_id, new_price):
        self.put_url = f"{self.sheety_price_url}/{row_id}"

        payload = {
            "price": {
                "lowestPrice": new_price
            }
        }
        res = requests.put(self.put_url, headers=self.headers, json=payload)
        return (res.json())