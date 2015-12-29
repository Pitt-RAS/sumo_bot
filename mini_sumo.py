import time

#load files
execfile("linesense2.py")
execfile("longrangemethod.py")
execfile("minisumo.py")
execfile("minisumo_motorcontrol	2.py")
execfile("mouse1.py")
execfile("rangesensor.py")
execfile("short_range_Sense.py")
execfile("shortrangemethod.py")

#Create objects	and variables
lineSensors= lineSensor_Class()
motors= Motors_Class()
longrange= longrange_Class()
shortrange= shortrange_Class()
mouse_data = mouse_pos(stat,x,y)
first = 'y'
origin = 'y'

##can move this function into the lineSensors class
def checkLines():
	if lineSensors.check1() == 1:
		motors.motor_move('x',0)
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check2() == 1:
		motors.motor_move('x',0)
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check3() == 1:
		motors.motor_move('x',0)
		motors.motor_move('a', 4)
		detect = 1
	elif lineSensors.check4() == 1:
		motors.motor_move('x',0)
		motors.motor_move('a', 4)
		detect = 1
	else:
		detect = 0
	return detect
	
def loop2():  #used in sense line origin part of flow chart
	while True: 
		if mouse_data[0] > 0 || mouse_data[1] >0:
			lines = checkLines
			if lines == 0:
				#all of these checks seem to lead to the same action in the flow chart?
				if mouse_data[1] > 0  && mouse_data[0] > 0:
					motors.motor_move('x',0)
					motors.motor_move('a', 2)
				elif mouse_data[0] < 0 && mouse_data[1] > 0:
					motors.motor_move('x',0)
					motors.motor_move('a', 2)
				elif mouse_data[0] > 0 && mouse_data[1] < 0:
					motors.motor_move('x',0)
					motors.motor_move('a', 2)
				elif mouse_data[0] < 0 && mouse_data[1] < 0:
					motors.motor_move('x',0)
					motors.motor_move('a', 2)
				else:
					break 
			else:
				motors.motor_move('x',0)
				motors.motor_move('a', 4)
		else:
			break 

##MAIN LOOP
while True:
	short = shortrange.rngsens
	while short > 2 && short < 15:
	##the part in the if should be added to the motor_move method so it doesn't need repeated
		if first == 'y':
			motors.motor_move('x',0)
			time.sleep(1)
			first = 'n'
		else:
			motors.motor_move('w',4)
			origin = 'n'
			lines = checkLines()
	long = longrange.rangesens
	if long > 10 && long < 80:
		##not sure what the computer vision methods look like
		##this is an outline
		if cv == 1: #> 300
			motors.motor_move('x',0)
			time.sleep(1)
			motors.motor_move('a',4)
			if mouse_data[0] < 0:
				if mouse y > 0:
					origin = 'n'
					break
				else:
					motors.motor_move('x',0)
					motors.motor_move('w',4)
			if mouse_data[0] > 0:
				motors.motor_move('x',0)
				motors.motor_move('d',4)
		elif cv == 0: #<300
			motors.motor_move('x',0)
			motors.motor_move('d',4)
			if mouse_data[0] > 0:
				motors.motor_move('x',0)
				motors.motor_move('d',4)
			else:
				motors.motor_move('x',0)
				motors.motor_move('a',4)
	lines = checkLines()
	if origin == 'y':
		if lines == 0:
			while True:
				if long > 10 && long < 80:
					break
				else:
				#this part needs work
					motors.motor_move('x',0)
					motors.motor_move('a',4)
					time.sleep(6) ##check time (sec) for 120 degrees
					motors.motor_move('x',0)
					loop2()
					motors.motor_move('d',0)
					time.sleep(4) #check time for 60 degrees
					loop2()
		else:
			while True:
				if long > 10 && long < 80:
					break
				else:
					degrees = 0
					while degrees <= 360:
						motors.motor_move('x',0)
						motors.motor_move('d',4)
						time.sleep(2) ##check how long it takes to turn 10 degrees
						loop2()
						degrees+=10
					break 
	lines = checkLines()
