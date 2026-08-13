#!/usr/bin/env python3
'''FlightData and Cheapest Flight finder'''


class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data, return_date):
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])
    if not all_flights:
        fldata_list = [FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )]
        return fldata_list[0]
    fldata_list = [FlightData(
            price= flight["price"],
            origin_airport=flight["flights"][0]["departure_airport"]["id"],
            destination_airport=flight["flights"][-1]["arrival_airport"]["id"],
            out_date=flight["flights"][0]["departure_airport"]["time"],
            return_date=return_date,
            stops=len(flight["flights"]) - 1
        ) for flight in all_flights]
    sorted_flights = sorted(fldata_list, key=lambda f:f.price)
    return(sorted_flights[0])
