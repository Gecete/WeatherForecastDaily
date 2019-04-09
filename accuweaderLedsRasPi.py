import requests
import json

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
verde=29
rojo=7
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.output(rojo, False)
GPIO.output(verde, False)
# api - endpoint
URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/307297?apikey=GZfFqIdbS5ObEpGju9TMJqYXz9XjKKo1"

URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/307297?apikey=CdfUdiGhheabSNU0Nme56GFU4IbfWtaC"

PARAMS = {
	'details': False,
	'metric': True,
	'language': 'es'
};

r = requests.get(url=URL, params=PARAMS)

data = r.json()
print(data)

print json.dumps(data, indent=2, sort_keys=True);

if data['DailyForecasts'][0]['Day']['Icon'] == 25 or data['DailyForecasts'][0]['Day']['Icon'] == 29 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 12 or data['DailyForecasts'][0]['Day']['Icon'] == 13 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 14 or data['DailyForecasts'][0]['Day']['Icon'] == 15 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 16 or data['DailyForecasts'][0]['Day']['Icon'] == 17 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 18 or data['DailyForecasts'][0]['Day']['Icon'] == 39 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 40 or data['DailyForecasts'][0]['Day']['Icon'] == 41 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 42 or data['DailyForecasts'][0]['Day']['Icon'] == 43 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 44:
	print("Lluvia")
	GPIO.output(rojo, True)
	time.sleep(3000)
else:
	print("Sin Lluvia")
	GPIO.output(verde, True)
	time.sleep(3000)
GPIO.output(rojo, False)
GPIO.output(verde, False)
sys.exit()
