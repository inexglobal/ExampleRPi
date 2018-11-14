import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)
def read(ch):
	channels= [0x00, 0x40, 0x10, 0x50, 0x20, 0x60, 0x30, 0x70] 
	command = 0x80 | channels[ch] # Enable Single-ended mode (toggle MSB, SD bit in datasheet)
	# ADS7828 address, 0x48(72)
	# Read data back from 0x00(00), 2 bytes
	# raw_adc MSB, raw_adc LSB
	data = bus.read_i2c_block_data(0x48,command,2)
	# Convert the data to 12-bits
	raw_adc = (data[0] & 0x0F) * 256 + data[1]
	return raw_adc
while 1 :
	# ADS7828 address, 0x48(72)
	# Send command byte
	#		0x80 (Single-Ended Inputs) | 0x00 (channel- AN0 selected) )
	for x in range(8):
		# Output data to screen
		print ("analog AN %d : %d" % (x,read(x)))	
	time.sleep(1)
	

