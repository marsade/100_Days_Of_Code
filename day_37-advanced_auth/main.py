#!/usr/bin/env python3
import requests
from datetime import datetime

USERNAME = "mars2"
TOKEN = "hjdfgjvswsl'ojjn"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hjdfgjvswsl'ojjn",
    "username": "mars2",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Push-ups Graph",
    "unit": "Rep",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime(year=2026, month=7, day=29)

pixel_add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# res = requests.post(url=pixel_add_endpoint, json=pixel_config, headers=headers)
# print(res.text)

update_pixel_endp = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "13"
}
# res = requests.put(url=update_pixel_endp, json=new_pixel_data, headers=headers)
# print(res.text)

del_pixel_endp = update_pixel_endp

res = requests.delete(url=del_pixel_endp, headers=headers)