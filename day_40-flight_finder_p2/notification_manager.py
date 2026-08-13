#!/usr/bin/env python3
'''Twilio Notification Manager Class'''
import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
class NotificationManager:
    def __init__(self, fl_price, dep, arr, out, in_, stops):
        self.acc_sid = os.getenv("TW_ACC_SID")
        self.auth = os.getenv("TW_AUTH")
        self.client = Client(self.acc_sid, self.auth)
        self.mail = os.getenv("SMTP_ADDRESS")
        self.ml_psw = os.getenv("SMTP_PASSWORD")
        if stops > 1:
            self.msg_body = f"Low price alert! Only USD{fl_price} to fly from {dep} to {arr}, with {stops} stops departing on {out} and returning {in_}"
        else:
            self.msg_body = f"Low price alert! Only USD{fl_price} to fly directly from {dep} to {arr}, departing on {out} and returning {in_}"

    def send_sms(self):
        message = self.client.messages \
            .create(
                body=self.msg_body,
                from_=os.getenv("TW_VIRTUAL_NUM"),
                to=os.getenv("TW_VERIFIED_NUM")
            )
        print(message.status)

    def send_whatsapp(self):
        message = self.client.messages \
            .create(
                body=self.msg_body,
                from_=f"whatsapp:{os.getenv("TW_VIRWP_NUM")}",
                to=f"whatsapp:{os.getenv("TW_WHATSAPP_NUM")}"
            )
        print(message.sid)

    def send_emails(self, to_addr):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.mail, password=self.ml_psw)
            connection.sendmail(
                from_addr=self.mail,
                to_addrs= to_addr,
                msg=self.msg_body
            )
