#!/usr/bin/env python3
import csv


# Opening without csv
# with open("weather_data.csv") as f:
#     data = f.readlines()

# Opening with csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])