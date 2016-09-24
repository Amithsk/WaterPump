import pyowm
import json
import requests
import json

def retrieveLocation():
  url = 'http://freegeoip.net/json'
  Res = requests.get(url)
  Temp= json.loads(Res.text)
  Location =''.join([Temp['city'],',',Temp['country_code']])
  return Location


def retrieveWeatherdetails():
#Retrieve location information
 Location = retrieveLocation()

#Retrieve weather information
 owm = pyowm.OWM('8a41803eb0d905c467564e6e4822d7d2')  # You MUST provide a valid API key

# Search for current weather 
 observation = owm.weather_at_place('Location')
 JSON = observation.to_JSON()
 JS = json.loads(JSON)
 return JS['Weather']['status'],JS['Weather']['humidity'],JS['Weather']['temperature']['temp_max'],JS['Weather']['temperature']['temp_min']



def weatherUpdate():
  retrieveWeatherdetails()

