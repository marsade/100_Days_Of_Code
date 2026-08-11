#!/usr/bin/env python3
'''Twilio Notification Manager Class'''
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
class NotificationManager:
    def __init__(self, fl_price, dep, arr, out, in_):
        self.acc_sid = os.getenv("TW_ACC_SID")
        self.auth = os.getenv("TW_AUTH")
        self.client = Client(self.acc_sid, self.auth)
        self.msg_body = f"Low price alert! Only ${fl_price} to fly from {dep} to {arr}, on {out} until {in_}"

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
