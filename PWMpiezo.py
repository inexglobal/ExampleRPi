import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
blink = GPIO.PWM(24,500)
blink.start(0)
while True:
	da=datetime.now()
	microsec=da.microsecond
	if microsec > 700000:
		blink.ChangeDutyCycle(50)
	else:
		blink.ChangeDutyCycle(0)
