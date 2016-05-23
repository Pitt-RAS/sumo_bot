import numpy as np
import sys,select
import cv2
import time
import os
import RPi.GPIO as GPIO
from minisumo_motorcontrol2 import Motors_Class
from lineSense2 import lineSensor_Class
from shortrangemethod import shortrange_Class
from minisumo_motorcontrol3 import Motors_Class2
#anything less than 15 switch to short range sensors 
motor1= Motors_Class()
lineSensors = lineSensor_Class()
shortrange= shortrange_Class()
motor2 = Motors_Class2()
cap= cv2.VideoCapture(0)
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
class longrange_Class:

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
 


	 
	def rangesens(self):
		global SPICLK
		global SPIMISO
		global SPIMOSI
		global SPICS
		global cap
		lastdist = 0
		potentiometer_adc = 7;
		r_sensor = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
		ret,frame = cap.read()
	        r,h,c,w = 250,150,400,150  # simply hardcoded the values
     
     		track_window = (c,r,w,h)
        # set up the ROI for tracking
        	roi = frame[r:r+h, c:c+w]
        	hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        	mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        	roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        	cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
				 
		set_volume = int(r_sensor)       
		voltage = (set_volume*3.3)/1024
		inv_distance = .005*(voltage)**2+.02816666*(voltage)+.0036
		distance = inv_distance**-1
		distance = int(distance)-8
		#print "l distance" + str(distance)
		if (0< distance and distance <= 70):
			if(lineSensors.check1() == 1):
				return distance
			elif(lineSensors.check2() == 1):
				return distance
			elif (lineSensors.check3()==1):
				return distance
			elif(lineSensors.check4() == 1):
				return distance
			ret ,frame = cap.read()
    			if ret == True:
        			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        			dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        			ret, track_window = cv2.meanShift(dst, track_window, term_crit)
       				 # Draw it on image
        			x,y,w,h = track_window
        			dist= (x+w)/2
        			avgd=lastdist-dist
        			img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
				cv2.imshow('img2',img2)
        			#while(avgd> 50 or avgd<-50):
                		x,y,w,h = track_window
                		avgd = dist-x
                		dist=x
        			lastdist=dist
        			if(dist> 300):
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                		return distance
                        		elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                		return distance
                        		elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                		return distance
                        		elif(lineSensors.check4() == 1):	
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                		return distance
					while(shortrange.rngsens() != 0):
						u=0
                			motor1.motor_move('a',8)
                			motor2.motor_move('a',8)
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                                return distance
                                        elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check4() == 1):
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                                return distance
        			elif(dist<200):
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                        		        return distance
                        		elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                		return distance
                        		elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                		return distance
                        		elif(lineSensors.check4() == 1):
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                		return distance
					while(shortrange.rngsens() != 0):
                                                u=0
                			motor1.motor_move('d',8)
                			motor2.motor_move('d',8)
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                                return distance
                                        elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check4() == 1):
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                                return distance
        			else:
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
						motor2.motor_move('s',8)
        		                        return distance
                        		elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                		return distance
                        		elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                		return distance
                        		elif(lineSensors.check4() == 1):
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                		return distance
                			while(shortrange.rngsens() != 0):
                                                u=0
					motor1.motor_move('w',8)
					motor2.motor_move('w',8)
					if(lineSensors.check1() == 1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check2() == 1):
						motor1.motor_move('a',8)
                                                motor2.motor_move('a',8)
                                                return distance
                                        elif (lineSensors.check3()==1):
						motor1.motor_move('s',8)
                                                motor2.motor_move('s',8)
                                                return distance
                                        elif(lineSensors.check4() == 1):
						motor1.motor_move('d',8)
                                                motor2.motor_move('d',8)
                                                return distance
	
		time.sleep(0.0001)		
		return distance

