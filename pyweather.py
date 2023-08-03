import requests, json
import apikey.py
# base URL
# https://openweathermap.org/current#zip
### 
# https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
###
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# ZIP = "55416"
# COUNTRY_CODE = "US"
# API_KEY from apikey.py (also included in gitignore) 

URL = BASE_URL + "zip=" + ZIP + "," + COUNTRY_CODE + "&appid=" + API_KEY

response = requests.get(URL)
if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
else:
   # showing the error message
   print("Error in the HTTP request")
