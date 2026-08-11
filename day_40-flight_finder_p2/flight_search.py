#!/usr/bin/env python3
'''Flight Finder'''
import os
import requests
from dotenv import load_dotenv


load_dotenv()
class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("SERPAPI_KEY")
        self.endpoint = os.getenv("SERPAPI_URL")
        self.params = {
            "engine": "google_flights",
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self._api_key,
        }

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        self.params["outbound_date"] = from_time
        self.params["return_date"] = to_time
        self.params["departure_id"] = origin_city_code
        self.params["arrival_id"] = destination_city_code
        self.params["stops"] = 1 if is_direct else 0
        res = requests.get(self.endpoint, params=self.params)
        res.raise_for_status()
        self.data = res.json()
        return self.data