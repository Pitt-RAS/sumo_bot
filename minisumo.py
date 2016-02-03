import time

#load files

from lineSense2 import lineSensor_Class
from longrangemethod import longrange_Class
from shortrangemethod import shortrange_Class
from minisumo_motorcontrol2 import Motors_Class
from minisumo_motorcontrol3 import Motors_Class2
from accelerometer import Accel

#Create objects	and variables
lineSensors= lineSensor_Class()
motors= Motors_Class()
motors2 = Motors_Class2()
longrange= longrange_Class()
shortrange= shortrange_Class()
mouse_data = mouse_pos(stat,x,y)
first = 'y'
origin = 'y'

##can move this function into the lineSensors class
def checkLines():
	if lineSensors.check1() == 1:
		motors.motor_move('a', 4)
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check2() == 1:
		moving('x')
		motors2.motor_move('x', 0)
		motors.motor_move('a', 4)
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check3() == 1:
		moving('x')
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check4() == 1:
		moving('x')
		motors.motor_move('a', 4)
		detect = 1
	else:
		detect = 0
	return detect
	
def loop2():  #used in sense line origin part of flow chart
	while True: 
		if mouse_data[0] > 0 or mouse_data[1] >0:
			lines = checkLines
			if lines == 0:
				#all of these checks seem to lead to the same action in the flow chart?
				if mouse_data[1] > 0  and mouse_data[0] > 0:
					moving('x')
					motors.motor_move('a', 2)
				elif mouse_data[0] < 0 and mouse_data[1] > 0:
					moving('x')
					motors.motor_move('a', 2)
				elif mouse_data[0] > 0 and mouse_data[1] < 0:
					moving('x')
					motors.motor_move('a', 2)
				elif mouse_data[0] < 0 and mouse_data[1] < 0:
					moving('x')
					motors.motor_move('a', 2)
				else:
					break 
			else:
				moving('x')
				motors.motor_move('a', 4)
		else:
			break 
		
def moving(dir):
	if dir = 'x':
		motors.motor_move('x', 0)
		motors2.motor_move('x', 0)
	if dir = 'a':
		motors.motor_move('a', 4)
		motors2.motor_move('a',4)
	if dir = 's':
		motors.motor_move('s',4)
		motors2.motor_move('s',4)
	if dir = 'd':
		motors.motor_move('d', 4)
		motors2.motor_move('d',4)
	if dir = 'w':
		motors.motor_move('w',4)
		motors2.motor_move('w', 4)

##MAIN LOOP
while True:
	short = shortrange.rngsens
	while short > 2 and short < 15:
	##the part in the if should be added to the motor_move method so it doesn't need repeated
		if first == 'y':
			moving('x')
			time.sleep(1)
			first = 'n'
		else:
			moving('w')
			origin = 'n'
			lines = checkLines()
	long = longrange.rangesens
	if long > 10 and long < 80:
		##not sure what the computer vision methods look like
		##this is an outline
		if cv == 1: #> 300
			moving('x')
			time.sleep(1)
			moving('a')
			if mouse_data[0] < 0:
				if mouse_y > 0:
					origin = 'n'
					break
				else:
					move('x')
					move('w')
			if mouse_data[0] > 0:
				move('x')
				moving('d')
		elif cv == 0: #<300
			moving('x')
			moving('d')
			if mouse_data[0] > 0:
				moving('x')
				moving('d')
			else:
				moving('x')
				moving('a')
	lines = checkLines()
	if origin == 'y':
		if lines == 0:
			while True:
				if long > 10 and long < 80:
					break
				else:
				#this part needs work
					moving('x')
					moving('a')
					time.sleep(6) ##check time (sec) for 120 degrees
					moving('x')
					loop2()
					moving('d')
					time.sleep(4) #check time for 60 degrees
					loop2()
		else:
			while True:
				if long > 10 and long < 80:
					break
				else:
					degrees = 0
					while degrees <= 360:
						moving('x')
						moving('d')
						time.sleep(2) ##check how long it takes to turn 10 degrees
						loop2()
						degrees+=10
					break 
	lines = checkLines()
