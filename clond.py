#!/usr/bin/env python
############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################
import time
import json
import RPi.GPIO as GPIO
from DHT11_Python import dht11
from beebotte import *

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)

API_KEY = 'd7f67dec2607f6ca0e904f458969f0e3'
SECRET_KEY = '574dc23358a92207f83cc908a95343037a71763e471151bb1aeedd8f3a2cfe02'
### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT(API_KEY,SECRET_KEY)
period = 5 ## Sensor data reporting period (5 seconds)

### Change channel name and resource names as suits you
temp_resource = Resource(bbt, 'RaspberryPi', 'Temp')
humid_resource = Resource(bbt, 'RaspberryPi', 'humi')

while True:
	### Assume
	result = instance.read()
	temperature=result.temperature
	humidity=result.humidity
	if result.is_valid():
		print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity))
		try:
			#Send temperature to Beebotte
			temp_resource.write(temperature)
			#Send humidity to Beebotte
			humid_resource.write(humidity)
		except Exception:
			## Process exception here
			print ("Error while writing to Beebotte")
	else:
		print ("Failed to get reading. Try again!")
	#Sleep some time
	time.sleep(period)
