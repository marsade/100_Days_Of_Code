#!/usr/bin/env python3
import os
import requests_cache
from data_manager import DataManager
from datetime import datetime
from dotenv import load_dotenv
from flight_search import FlightSearch
from pprint import pprint


load_dotenv()
requests_cache.install_cache(
    "flight_cache",
    expire_after=3600,
    urls_expire_after={
        os.getenv("SHEET_URL"): requests_cache.DO_NOT_CACHE
    }
)

search_flight = FlightSearch()
sheet_data = DataManager()
pprint(sheet_data.get_prices())
