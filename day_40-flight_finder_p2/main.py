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

DEP_IATA_CODE = "ECN"


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
    print(f"Getting direct flights for {sh["iataCode"]}")
    fl_data = search_flight.check_flights(DEP_IATA_CODE, sh["iataCode"], one_month, stay_till)
    return_date = fl_data["search_parameters"]["return_date"]
    cheapest_flight = find_cheapest_flight(fl_data, return_date=return_date)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight found  for {sh["iataCode"]}. Looking for indirect flights...")
        fl_data = search_flight.check_flights(DEP_IATA_CODE, sh["iataCode"], one_month, stay_till, is_direct=False)
        return_date = fl_data["search_parameters"]["return_date"]
        cheapest_flight = find_cheapest_flight(fl_data, return_date=return_date)
    print(f"Cheapest flight for {sh["iataCode"]} found: {cheapest_flight.price}")
    if cheapest_flight.price < sh["lowestPrice"]:
        print("Lower than sheet price. Updating sheet...")
        print(sheet_data.update_lowest_price(sh["id"], cheapest_flight.price))
        NotificationManager(cheapest_flight.price, "ECN", sh["iataCode"], one_month, stay_till).send_sms()
        NotificationManager(cheapest_flight.price, "ECN", sh["iataCode"], one_month, stay_till).send_whatsapp()
    else:
        print("Sheet Price Lower... skipping update")
