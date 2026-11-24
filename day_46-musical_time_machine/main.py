#!/usr/bin/env python3
'''Musical Time Machine with Spotify and Beautiful Soup'''
import datetime as dt
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

yt = YTMusic("browser.json")
db_base_url = "https://appbrewery.github.io/bakeboard-hot-100/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:160.0) Gecko/20100101 Firefox/160.0"
}

def avoidDuplicates(text):
    dup_num = 1
    text = text.split(")")
    last_num = text[0][-1:]
    if last_num.isdigit():
        str_split = text[0][:-1]
        dup_count = int(last_num) + dup_num
        text = str_split + f"{str(dup_count)})"
        res = "".join(text)
    else:
        text += f"({str(dup_num)})"
        res = "".join(text)

    return res 


try:
    usr_date = input("Which year do you want to travel to? Type it in this format YYYY-MM-DD:\n")
    travel_date = dt.date.fromisoformat(usr_date)
    travel_date_str = travel_date.strftime("%Y-%m-%d")
except ValueError:
    print("Invalid input. Please put in a correct date")

db_full_url = f"{db_base_url}{travel_date_str}/"

response = requests.get(db_full_url, headers=headers)

bb_webpage = response.text
bb_soup = BeautifulSoup(bb_webpage, "html.parser")

song_names = [son.getText() for son in bb_soup.find_all(name="h3", class_="chart-entry__title")]


existing_pl = yt.get_library_playlists()

pl_name = f"{travel_date_str} Time Machine"

dup_status = False
for pls in existing_pl:
    if pl_name == pls["title"]:
        new_pl_name = avoidDuplicates(pl_name)
        dup_status = True
if dup_status:
    playlist = yt.create_playlist(new_pl_name, f"Billboard Top 100 songs on {travel_date_str}")
else:
    playlist = yt.create_playlist(pl_name, f"Billboard Top 100 songs on {travel_date_str}")
