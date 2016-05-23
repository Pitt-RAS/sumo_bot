import time
from lineSense2 import lineSensor_Class 
from minisumo_motorcontrol2 import Motors_Class
from longrangemethod import longrange_Class
from shortrangemethod import shortrange_Class
lineSensors= lineSensor_Class()
motors= Motors_Class()
longrange= longrange_Class()
shortrange= shortrange_Class()

motors.motor_move("w",4)

while(True):
	if(1==lineSensors.check1()):
		motors.motor_move("x",0)
		time.sleep(1)
		motors.motor_move("s",4)
	elif(1==lineSensors.check2()):
		motors.motor_move('x',0)
		time.sleep(1)
		motors.motor_move('s',4)
	elif(1==lineSensors.check3()):
		motors.motor_move('x',0)
		time.sleep(1)
		motors.motor_move('s',4)
	elif(1==lineSensors.check4()):
		motors.motor_move('x',0)
		time.sleep(1)
		motors.motor_move('s',4)
	elif(shortrange.rngsens()>3):
		motors.motor_move('x',0)
		time.sleep(1)
		motors.motor_move('w',4)
	elif(shortrange.rngsens()<20):
		motors.motor_move('x',0)
		time.sleep(1)
		motors.motor_move('w',4)
	elif(longrange.rangesens()>15):
		motors.motor_move('x', 0)
		time.sleep(1)
		motors.motor_move('w', 4)
	elif(longrange.rangesens()<75):
		motors.motor_move('x', 0)
		time.sleep(1)
		motors.motor_move('w', 0)
