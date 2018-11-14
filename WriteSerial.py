import serial
import time
import io 
ser = serial.Serial('/dev/ttyUSB0',19200, timeout=0.25) # open serial port on USB
counter = 0
while 1 :
	counter = counter + 1
	conv_data = str(counter) 
	ser.write(conv_data.encode('ascii')) # write a string
	ser.write(b'\n')  # write a '\n' terminated line
	time.sleep(.5) # delay 0.5 s
