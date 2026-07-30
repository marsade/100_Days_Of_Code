# Day 37 - Advanced Authentication, Post Requests & Headers
## Building
- Habits Tracker

## Overview
Types of requests:
- GET:
```py 
requests.get()
```
Asking an external system for some piece of data
- POST:
```py
request.post()
```
Giving an external system some data. Only response interested in is if successful or not
- PUT:
```py
requests.put()
```
Updating a piece of data in the external service. 
- DELETE
```py
requests.delete()
```
Used to delete a piece of data in the external service. 

## Headers
The header is the part that contains some relevant pieces of information. In previous projects, we simply send our API key as a parameter along with the get request but that can be dangerous because all our secret stuff is in the request itself. So if anyone is monitoring this, they will be able to see that information and they might be able to steal your API key. SO for some API providers, you might see that they want you to provide the authentication in the header. 