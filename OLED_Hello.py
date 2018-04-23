import time
import Adafruit_SSD1306

from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 1

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Initialize library.
disp.begin()
# Clear display.
disp.clear()
count=0
while(1):
	count=count+1
	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	width = disp.width
	height = disp.height  
	image = Image.new('1', (width, height))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)
	# Load default font.
	#font = ImageFont.load_default()
	# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
	# Some other nice fonts to try: http://www.dafont.com/bitmap.php
	font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
	draw.text((0,0), 'Hello',font=font, fill=1)
	draw.text((30,20), 'World!',font=font, fill=1)
	draw.text((0,40),str(count),font=font, fill=1)
	
	# Display image.
	disp.image(image)
	disp.display()
