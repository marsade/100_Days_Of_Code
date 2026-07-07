# Day 33 - APIs
## Overview
An API is a set of commands, functions, protocols and objects that programmers can use to create software or interact with an external system. Essentially the API is an interface, basically a barrier between your program and an external system. And what programmers do is try to use the rules that the API has prescribed to make a request to the external system for some peice of data. nd if the request is structured according to all of the requirements that the external system has set out in their API then they will respond to you appropriately

## API Endpoint
One of the most important features of an API is its endpoint, and you can imagine that as a location of the service. It is just a URL.

## API Request
In python, we use the requests library get a response from an API. Response codes have different meanings, they mostly are there to tell us whether our requests succeeded or not.
```py
import requests

response = requests.get(url=url)
print(response)
```
## Response Codes
1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You screwed up
5XX: I (Server) screwed up
