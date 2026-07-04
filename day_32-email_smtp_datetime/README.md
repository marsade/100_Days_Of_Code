# Day 32 - Email SMTP & Datetime
## Overview
SMTP stands for Single Mail Transfer Protocol. And it contains all the rules of how an email is received by mail servers and passed on to the next mail server and how email can be sent around the internet. 
In python there is a module called `smtplib` that allows us to use smtp to send our email to any address on the internet. 
## Creating a connection with SMTP
To create a connection to a mail server, we need to create an SMTP object and secure it with TLS
```py
connection = smtplib.SMTP("smtp.gmail.com", "kickstop@gmail.com")
connection.starttls()
connection.close()
```
or with a context manager
```py
with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
```
## Datetime
The Datetime module gives us access to dates and time in python
```py
import datetime as dt

dt.datetime.now()
print(now)
```

## Warning: For security reasons, most of the code in this day wasn't uploaded to github. Sorry for the inconvenience.