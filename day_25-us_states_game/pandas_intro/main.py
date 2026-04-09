#!/usr/bin/env python3
import csv


# Opening without csv
with open("weather_data.csv") as f:
    data = f.readlines()

# Opening with csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

import pandas

# Reading CSV with pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

# # Pandas series method to find mean
print(data["temp"].mean())

# # Pandas series method to find max
print(data["temp"].max())

# # Another way to access columns
print(data.condition)

# How to get data in the rows
print(data[data["day"] == "Monday"])

# #Print the row where the temperature is the max
print(data[data["temp"] == data["temp"].max()])

# Convert Monday's temperature into farenheit
mon_ctemp = data[data.day == "Monday"].temp[0]
mon_ftemp = (mon_ctemp * 1.8) + 32
print(mon_ftemp)

# HOw to create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Mars"],
    "scores": [76, 56, 85]
}
dataf = pandas.DataFrame(data_dict)
print(dataf)
dataf.to_csv("new_data.csv")