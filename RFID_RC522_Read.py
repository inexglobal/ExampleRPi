#!/usr/bin/env python

import signal
import time
import sys
import RPi.GPIO as GPIO
from pirc522 import RFID

''' # RPi pin name
SDA = 8
SCK = 11
MOSI = 10
MISO = 9
IPQ = 24
RST = 25
'''

rdr = RFID(pin_rst=25,pin_irq=24,pin_mode = GPIO.BCM)

print ('Press Ctrl-C to quit.')
try:
	while 1:
		rdr.wait_for_tag() # จนกว่าจะแท็ก RFID
		(error, tag_type) = rdr.request() # อ่านข้อมูลในแท็ก ฑโณฏ
		if not error:
			(error, uid) = rdr.anticoll() # อ่านค่า ID
			if not error:
				print("[%d] Card read UID: %s" % (time.time(),str(uid)))
				time.sleep(1)
except:
	pass
finally:
	rdr.cleanup()
	sys.exit()
