#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
class keypad():
	def __init__(self,Row,Column):	
		GPIO.setmode(GPIO.BCM)
		self.KEYPAD = [
					[1,2,3,"A"],
					[4,5,6,"B"],
					[7,8,9,"C"],
					["*",0,"#","D"]
					]
		self.ROW    = Row
		self.COLUMN = Column  
		
	def getKey(self):
         
        # Set all columns as output low
		for j in range(len(self.COLUMN)):
			GPIO.setup(self.COLUMN[j], GPIO.OUT)
			GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
		for i in range(len(self.ROW)):
			GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
		rowVal = -1
		for i in range(len(self.ROW)):
			tmpRead = GPIO.input(self.ROW[i])
			if tmpRead == 0:
				rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
		if rowVal <0 or rowVal >3:
			self.exit()
			return
         
        # Convert columns to input
		for j in range(len(self.COLUMN)):
			GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
		GPIO.setup(self.ROW[rowVal], GPIO.OUT)
		GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 3.
		colVal = -1
		for j in range(len(self.COLUMN)):
			tmpRead = GPIO.input(self.COLUMN[j])
			if tmpRead == 1:
				colVal=j
                 
        # if colVal is not 0 thru 3 then no button was pressed and we can exit
		if colVal <0 or colVal >3:
			self.exit()
			return
			
        # Return the value of the key pressed
		self.exit()
		return self.KEYPAD[rowVal][colVal]
         
	def exit(self):
		# Reinitialize all rows and columns as input at exit
		for i in range(len(self.ROW)):
			GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
		for j in range(len(self.COLUMN)):
			GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
                
kp = keypad(Row=[21,20,16,7],Column=[26,19,13,6])
st_press=0
digit_str=''
while 1:     
    # Loop while waiting for a keypress
	digit = None
	digit = kp.getKey()
	if digit == None:
		st_press=1
	else:
		if st_press:
			# Print the result
			digit_str+=str(digit)
			print (digit_str,end='\r')
			st_press=0
			time.sleep(0.3)
