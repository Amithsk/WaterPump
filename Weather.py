import pyowm
import json

owm = pyowm.OWM('8a41803eb0d905c467564e6e4822d7d2')  # You MUST provide a valid API key


# Search for current weather 
observation = owm.weather_at_place('Bangalore,IN')
w = observation.get_weather()

JSON = observation.to_JSON()
JS = json.loads(JSON)
print (JS['Weather']['status'])
print (JS['Weather']['humidity'])
print (JS['Weather']['temperature']['temp_max'])
