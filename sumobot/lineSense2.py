import time
import os
import RPi.GPIO as GPIO
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

    #anything less than 15 switch to short range sensors 
class lineSensor_Class:

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
       
      # 10k trim pot connected to adc #0
  		
  		
     
    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	def readadc(self, adcnum, clockpin, mosipin, misopin, cspin):
		if ((adcnum > 7) or (adcnum < 0)):
                	return -1
       		GPIO.output(cspin, True)
 
        	GPIO.output(clockpin, False)  # start clock low
        	GPIO.output(cspin, False)     # bring CS low
     
        	commandout = adcnum
        	commandout |= 0x18  # start bit + single-ended bit
        	commandout <<= 3    # we only need to send 5 bits here
        	for i in range(5):
                	if (commandout & 0x80):
                        	GPIO.output(mosipin, True)
                	else:
                        	GPIO.output(mosipin, False)
                	commandout <<= 1
                	GPIO.output(clockpin, True)
                	GPIO.output(clockpin, False)
     
        	adcout = 0
            # read in one empty bit, one null bit and 10 ADC bits
        	for i in range(12):
                	GPIO.output(clockpin, True)
                	GPIO.output(clockpin, False)
                	adcout <<= 1
                	if (GPIO.input(misopin)==1):
                        	adcout |= 0x1
     
        	GPIO.output(cspin, True)
            
        	adcout >>= 1       # first bit is 'null' so drop it
        	return adcout
     

	def check1(self):
      # change these as desired - they're the pins connected from the
      # SPI port on the ADC to the Cobbler
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
  		potentiometer_adc = 2
    		done=0
		i=0
      #last_read = 0       # this keeps track of the last potentiometer value
      #tolerance = 5       # to keep from being jittery we'll only change
      # volume when the pot has moved more than 5 'counts'
		reading=0
  		while (i<10):
    			trim_pot = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    			reading = reading + trim_pot
    			i += 1

  		done = reading/10
  		if (done<50):
    			return 1
  		else:
    			return 0

	def check2(self):
      # change these as desired - they're the pins connected from the
      # SPI port on the ADC to the Cobbler
        # 10k trim pot connected to adc #0
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
  		potentiometer_adc = 3
  		reading = 0
  		done = 0
  		i = 0
  #last_read = 0       # this keeps track of the last potentiometer value
      #tolerance = 5       # to keep from being jittery we'll only change
      # volume when the pot has moved more than 5 'counts'
  		while (i<10):

    			trim_pot = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    			reading = reading + trim_pot
    			i += 1

  		done = reading/10
  		if (done<50):
    			return 1
  		else:
    			return 0

	def check3(self):
      # change these as desired - they're the pins connected from the
      # SPI port on the ADC to the Cobbler
   # set up the SPI interface pins
      # 10k trim pot connected to adc #0
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
  		potentiometer_adc = 4
  		reading = 0
 		done = 0
  		i = 0
      #last_read = 0       # this keeps track of the last potentiometer value
      #tolerance = 5       # to keep from being jittery we'll only change
      # volume when the pot has moved more than 5 'counts'
  		while (i<10):

    			trim_pot = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    			reading = reading + trim_pot
    			i += 1

  		done = reading/10
  		if (done<50):
    			return 1
  		else:
    			return 0

	def check4(self):
      # change these as desired - they're the pins connected from the
      # SPI port on the ADC to the Cobbler
    
      # set up the SPI interface pins     
      # 10k trim pot connected to adc #0
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
		potentiometer_adc = 5
  		reading = 0
  		done = 0
  		i = 0
      #last_read = 0       # this keeps track of the last potentiometer value
      #tolerance = 5       # to keep from being jittery we'll only change
      # volume when the pot has moved more than 5 'counts'
  		while (i<10):
  		  	trim_pot = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
  		  	reading = reading + trim_pot
    		i += 1

  		done = reading/10
  		if (done<50):
    			return 1
  		else:
    			return 0
