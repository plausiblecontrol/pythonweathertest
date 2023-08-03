import requests, json
from apikey import *
# base URL
# https://openweathermap.org/current#zip
### 
# https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
###
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
ZIP = "55416"
COUNTRY_CODE = "US"

# API_KEY from apikey.py (also included in gitignore) 

URL = BASE_URL + "zip=" + ZIP + "," + COUNTRY_CODE + "&appid=" + API_KEY + "&units=imperial"

response = requests.get(URL)
if response.status_code == 200:
  data = response.json()
  main = data['main']
  temperature = main['temp']
  humidity = main['humidity']
  print(f"Weather for {ZIP} is:")
  print(f"Temperature: {temperature}°F")
  print(f"Humidity: {humidity} %RH")
else:
  print("Error in the HTTP request")
