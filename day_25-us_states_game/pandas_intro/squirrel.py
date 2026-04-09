#!/usr/bin/env python3
'''Finding the Census of Squirrel Fur Colors'''
import pandas


data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_cl = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
black_cl = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
red_cl = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()

print(grey_cl, red_cl, black_cl)
cl_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_cl, red_cl, black_cl]
}
cl_df = pandas.DataFrame(cl_dict)
cl_df.to_csv("squirrel_count.csv")