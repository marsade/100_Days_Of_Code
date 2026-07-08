# Day 35 - API Keys, Authentication. Environment Variables and Sending SMS
## Overview
An API key is way that the API provider can track how much you're using their API and to authorise or deny access.

## Building
Rain Alert App

## Environment Variables
There's two main uses for environment variables. One is for convenience. FOr example, if you had an application that was sending emails out to your clients, then your client base emails may change everyday. SO certain variables that are being used in your code base could be set as environment variables. A second reason might be security. So when developing software, you might be uploading the code base anywhere. And its usually not a good idea to have aunthentication keys or API keys stored in the same place as the rest of your code. So essentially, environment variables allow us to seperate where we store our sensitive data from the rest of our code. 
```bash
export API_KEY="APIKEY"
```