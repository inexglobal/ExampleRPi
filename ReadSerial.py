import serial
ser = serial.Serial('/dev/ttyUSB0',19200, timeout=0.25) # open serial port on USB
while 1 :
	#x = ser.read()          # read one byte
	#s = ser.read(10)        # read up to ten bytes (timeout)
	#line = ser.readline()   # read a '\n' terminated line
	reading = ser.readline().decode('utf-8')
	if(reading):
		# reading is a string...do whatever you want from here
		print(reading)
	else:
		print('No data..');
