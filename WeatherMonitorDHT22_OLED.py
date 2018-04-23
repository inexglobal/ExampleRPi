import RPi.GPIO as GPIO
import Adafruit_SSD1306
from DHT_Python import dht22
from PIL import Image,ImageDraw,ImageFont
import time
import datetime


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4 instance
instance = dht22.DHT22(pin=4)
msgTime = ""
msgTemp = ""
msgHumi = ""

disp = Adafruit_SSD1306.SSD1306_128_64(rst=1)
disp.begin()
disp.clear()
width = disp.width
height = disp.height

while True:
	result = instance.read()
	datenow=datetime.datetime.now()
	if result.is_valid():
		msgTime=datenow.strftime("%H:%M:%S")
		msgTemp="T: %.1f C" % result.temperature
		msgHumi="H: %.1f %%" % result.humidity
	time.sleep(1)
	image = Image.new('1', (width, height))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
	draw.text((0,0),msgTime,font=font, fill=1)
	draw.text((0,20),msgTemp,font=font, fill=1)
	draw.text((0,40),msgHumi,font=font, fill=1)			
	disp.image(image)
	disp.display()
