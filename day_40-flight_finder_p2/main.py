#!/usr/bin/env python3
import datetime as dt
import os
import requests_cache
from data_manager import DataManager
from dotenv import load_dotenv
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint


load_dotenv()
requests_cache.install_cache(
    "flight_cache",
    expire_after=3600,
    urls_expire_after={
        os.getenv("SHEET_URL"): requests_cache.DO_NOT_CACHE
    }
)

one_month_dt = dt.datetime.today() + dt.timedelta(days=30)
stay_till_dt = one_month_dt + dt.timedelta(days=45)

one_month = one_month_dt.strftime("%Y-%m-%d")
stay_till = stay_till_dt.strftime("%Y-%m-%d")

sheet_data = DataManager()
sheet = sheet_data.get_prices()

search_flight = FlightSearch()
for sh in sheet:
    fl_data = search_flight.check_flights("ECN", sh["iataCode"], one_month, stay_till)
    return_date = fl_data["search_parameters"]["return_date"]
    flights_list = fl_data.get("best_flights", []) + fl_data.get("other_flights", [])

    cheapest_flight = find_cheapest_flight(flights_list, return_date=return_date)
    print("Cheapest Flight Found: ", cheapest_flight)
    if cheapest_flight < sh["lowestPrice"] and cheapest_flight != "N/A":
        print(sheet_data.update_lowest_price(sh["id"], cheapest_flight))
        NotificationManager(cheapest_flight, "ECN", sh["iataCode"], one_month, stay_till).send_sms()
        NotificationManager(cheapest_flight, "ECN", sh["iataCode"], one_month, stay_till).send_whatsapp()

    else:
        print("Sheet Price Lower... skipping update")
