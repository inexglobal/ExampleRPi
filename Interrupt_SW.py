import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
input_pin = 13
def button_pressed(channel):
	print ("Button Pressed")
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(input_pin, GPIO.RISING, callback=button_pressed,
bouncetime=300)
while(1):
	pass
