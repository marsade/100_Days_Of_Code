#!/usr/bin/env python3
'''Amazon Price Tracker'''
import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.message import EmailMessage
SITE = "https://appbrewery.github.io/instant_pot/"


load_dotenv()
target_price = 100
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:160.0) Gecko/20100101 Firefox/160.0"
}
response = requests.get(SITE, headers=headers)
site_text  = response.text
az_soup = BeautifulSoup(site_text, "html.parser")
itm = az_soup.select(".aok-offscreen")
itm_text = itm[0].getText()
itm_price = float(itm_text.split("$")[1])


def create_email(page, price):
    prod = page.find(name="span", id="productTitle").getText()
    prod_name = " ".join(prod.split())
    mail_content = f"{prod_name} is now {price}\n{SITE}"
    return mail_content


def send_email(to, content):
    mail = os.getenv("MY_EMAIL")
    pwd = os.getenv("MY_PASS")
    msg = EmailMessage()
    msg["Subject"] = "Amazon Price Alert!"
    msg["From"] = mail
    msg["To"] = to
    msg.set_content(f"{content}", charset="utf-8")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=pwd)
        connection.send_message(msg)



if itm_price <= target_price:
    cont = create_email(az_soup, itm_price)
    send_email(os.getenv("TO_EMAIL"), cont)
