#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from beebotte import *
LED_pin=5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin, GPIO.OUT)
blink = GPIO.PWM(LED_pin,500)
blink.start(0)
API_KEY = 'd7f67dec2607f6ca0e904f458969f0e3'
SECRET_KEY= '574dc23358a92207f83cc908a95343037a71763e471151bb1aeedd8f3a2cfe02'
### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT(API_KEY,SECRET_KEY)
while True:
	try:
		# Read from Beebotte return json
		records = bbt.read('RaspberryPi','valDuty')
		print (records)
		# Get data from json
		valpwm=records[0]['data']
		print (valpwm)
		blink.ChangeDutyCycle(valpwm)
	except Exception:
		print ("Error while writing to Beebotte")
