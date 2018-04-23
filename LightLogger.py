import time
import smbus
import datetime
bus = smbus.SMBus(1) #(512MB)
addr = 0x23 # i2c adress
while True:
	data = bus.read_i2c_block_data(addr,0x10)
	lum=(data[1] + (data[0]<<8) / 1.2)
	date=str(datetime.datetime.now())
	with open("BH1750.txt", "a") as text_file:
		text_file.write("DateTime: %s Luminosity: %.2f lx\n" % (date,lum,))
	time.sleep(0.5)
