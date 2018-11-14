#!/usr/bin/env python

import time
import sys
import RPi.GPIO as GPIO
import Adafruit_SSD1306
from pirc522.rfid import RFID   
from PIL import Image,ImageDraw,ImageFont

disp = Adafruit_SSD1306.SSD1306_128_64(rst=1)
disp.begin()
disp.clear()
width = disp.width
height = disp.height                        

''' # RPi pin name
SDA = 8
SCK = 11
MOSI = 10
MISO = 9
IPQ = 24
RST = 25

'''

rdr = RFID(pin_rst=25,pin_irq=24,pin_mode = GPIO.BCM)
counter_error = 0
_str = "Please tap"
print ('Press Ctrl-C to quit.')
try:
	while 1:
		(error, tag_type) = rdr.request()
		if not error:
			(error, uid) = rdr.anticoll()#อ่านค่า ID
			if not error:
				# แสดงในรูปแบบเลขฐานสิบหก
				_str = ' %x%x%x%x' % (uid[0],uid[1],uid[2],uid[3]) 
				counter_error=0
		else:
			counter_error = counter_error+1
			if (counter_error > 2):
				_str = "Please tap"	
		image = Image.new('1', (width, height))
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
		draw.text((0,20),_str,font=font, fill=1)			
		disp.image(image)
		disp.display()
except:
	pass
finally:
	rdr.cleanup()
	sys.exit()
