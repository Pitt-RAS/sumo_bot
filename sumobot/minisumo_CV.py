import numpy as np
from lineSense2 import lineSensor_Class
from minisumo_motorcontrol2 import Motors_Class
from minisumo_motorcontrol3 import Motors_Class2
import sys, select
import cv2

lineSensors = lineSensor_Class()
motors= Motors_Class()
motors2= Motors_Class2()
cap = cv2.VideoCapture(0)

# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
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
direct='w'
lastdist=0
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
	motors.motor_move(direct,4)
        motors2.motor_move(direct,4)
	lineSensors.check1()
	lineSensors.check2()
	lineSensors.check3()
	lineSensors.check4()
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
	dist= (x+w)/2
	avgd=lastdist-dist
	while(avgd> 50 or avgd<-50):
		x,y,w,h = track_window
		avgd = dist-x
		dist=x
	lastdist=dist
        if(dist> 300):
                motors.motor_move('a',7)
                motors2.motor_move('a',7)
        elif(dist<200):
                motors.motor_move('d',7)
                motors2.motor_move('d',7)
	else:
		motors.motor_move('w',4)
		motors2.motor_move('w',4)

        #img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        #cv2.imshow('img2',img2)
	print("x+w/2")
	print((x+w)/2)
	print("y+h/2")
	print((y+h)/2)
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break

    else:
        break

cv2.destroyAllWindows()
cap.release()
