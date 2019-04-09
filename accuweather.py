import requests
import json
import numpy as np
import cv2

# api-endpoint
URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/307297?apikey=APIKEY"

PARAMS = {'details': False,
		  'metric': True,
		  'language': 'es'};

r = requests.get(url=URL, params=PARAMS)

data = r.json()
print(data)
print json.dumps(data, indent=2, sort_keys=True);
blank_image = np.zeros((500, 500, 3), np.uint8)
#todos los iconos de lluvia
if data['DailyForecasts'][0]['Day']['Icon'] == 25 or data['DailyForecasts'][0]['Day']['Icon'] == 29 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 12 or data['DailyForecasts'][0]['Day']['Icon'] == 13 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 14 or data['DailyForecasts'][0]['Day']['Icon'] == 15 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 16 or data['DailyForecasts'][0]['Day']['Icon'] == 17 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 18 or data['DailyForecasts'][0]['Day']['Icon'] == 39 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 40 or data['DailyForecasts'][0]['Day']['Icon'] == 41 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 42 or data['DailyForecasts'][0]['Day']['Icon'] == 43 or \
		data['DailyForecasts'][0]['Day']['Icon'] == 44:
	print("Lluvia")
	#BGR  Azul
	blank_image[:, :] = (255, 0, 0)
	image = blank_image
	cv2.imshow("imagen", image)
	cv2.waitKey(10000);
else:
	#BGR Amarillo
	print("Sin Lluvia")
	blank_image[:, :] = (0, 255, 255)
	image = blank_image
	cv2.imshow("imagen", image)
	cv2.waitKey(10000);
