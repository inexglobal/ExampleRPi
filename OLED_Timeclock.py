import time
import datetime
import Adafruit_SSD1306

from PIL import Image,ImageDraw,ImageFont
# Raspberry Pi pin configuration:
RST = 1
# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
last_sec=0
while(1):
	datenow=datetime.datetime.now()
	if datenow.second!=last_sec:
		str_weekday=datenow.strftime("%A")
		str_date=datenow.strftime("%d/%m/%Y")
		str_time=datenow.strftime("%H:%M:%S")
		last_sec=datenow.second
		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.
		width = disp.width
		height = disp.height  
		image = Image.new('1', (width, height))
		# Get drawing object to draw on image.
		draw = ImageDraw.Draw(image)
		# Load default font.
		font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',28)
		draw.text((0,18),str_time,font=font, fill=1)
		font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',18)
		draw.text((0,45),str_date,font=font, fill=1)
		draw.text((0,0),str_weekday,font=font, fill=1)
		# Display image.
		disp.image(image)
		disp.display()
	
