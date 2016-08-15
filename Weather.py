import pyowm

owm = pyowm.OWM('8a41803eb0d905c467564e6e4822d7d2')  # You MUST provide a valid API key

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather 
observation = owm.weather_at_place('Bangalore,IN')
w = observation.get_weather()
print(w)

Humidity=w.get_humidity()
Temp = w.get_temperature('celsius')

print(Temp)
print(Humidity)
