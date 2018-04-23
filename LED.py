#!/usr/bin/env python
############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################
import RPi.GPIO as GPIO
import time
import json
from beebotte import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED_pin=5
GPIO.setup(LED_pin,GPIO.OUT)
API_KEY = 'd7f67dec2607f6ca0e904f458969f0e3'
SECRET_KEY= '574dc23358a92207f83cc908a95343037a71763e471151bb1aeedd8f3a2cfe02'
### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT(API_KEY,SECRET_KEY)
while True:
	try:
		# Read from Beebotte return json
		records = bbt.read('RaspberryPi','StLED')
		print (records)
		# Get data from json
		StLED=records[0]['data']
		print (StLED)
		GPIO.output(5,StLED)
	except Exception:
		print ("Error while writing to Beebotte")
