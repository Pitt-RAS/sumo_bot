import time
import os
import RPi.GPIO as GPIO

#anything less than 15 switch to short range sensors
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
class shortrange_Class:

	def __init__(self):

		GPIO.setmode(GPIO.BCM)
		global SPICLK 
  		global SPIMISO 
  		global SPIMOSI
  		global SPICS
   
      # set up the SPI interface pins
  		GPIO.setup(SPIMOSI, GPIO.OUT)
  		GPIO.setup(SPIMISO, GPIO.IN)
  		GPIO.setup(SPICLK, GPIO.OUT)
  		GPIO.setup(SPICS, GPIO.OUT)
		GPIO.setmode(GPIO.BCM)


	def readadc(self, adcnum, clockpin, mosipin, misopin, cspin):
		if ((adcnum > 7) or (adcnum < 0)):
			return -1
		GPIO.output(cspin, True)
 	
		GPIO.output(clockpin, False)  
		GPIO.output(cspin, False)     
	 
		commandout = adcnum
		commandout |= 0x18  
		commandout <<= 3    
		for i in range(5):
			if (commandout & 0x80):
				GPIO.output(mosipin, True)
			else:
				GPIO.output(mosipin, False)
			commandout <<= 1
			GPIO.output(clockpin, True)
			GPIO.output(clockpin, False)
	 
		adcout = 0

		for i in range(12):
			GPIO.output(clockpin, True)
			GPIO.output(clockpin, False)
			adcout <<= 1
			if (GPIO.input(misopin)==1):
				adcout |= 0x1
	 
		GPIO.output(cspin, True)
			
		adcout >>= 1      
		return adcout
	 
	 
	def rngsens(self):
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
    		potentiometer_adc = 1;
		distance=0	
		s_sensor = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
		if (s_sensor != 9):	
			distance=(((6762/((s_sensor)-9))-4)/10)+1
			print "distance" + str(distance)
		time.sleep(0.1)
		return distance	
