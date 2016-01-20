from lineSense2 import lineSensor_Class()
from longrangemethod import longrange_Class()
from shortrangemethod import shortrange_Class()
from minisumo_motorcontrol2 import Motors_Class()
from Adafruit_LSM303 import Adafruit_LSM303
	
lineSensors= lineSensor_Class()
motors= Motors_Class()
longrange= longrange_Class()
shortrange= shortrange_Class()

short = shortrange.rngsens
long = longrange.rangesens
l1 = lineSensors.check1()
l2 = lineSensors.check2()
l3 = lineSensors.check3()
l4 = lineSensors.check4()
ax, ay, vx, vy, r_mx, r_my = Adafruit_LSM303.mat_accel()

def pressToContinue():
	command = rawinput('Press 1 to continue')
	if command == 1:
		continue
	else:
		break


while True:
	#Range Sensors
	print('Testing Short Range')
	pressToContinue()
	if short < 0 or short > 15: 
		break
	else:
		print('short = ', short)
	print('Testing Long Range')
	pressToContinue()
	if long < 10 or long > 80:
		break
	else:
		print('long = ', long)
		
	#line sensors
	print('Testing line sensors')
	pressToContinue()
	print('place left corner over line')
	pressToContinue()
	if (l1 == 1):
		break
	else:
		print ('l1 working')
	print('place tr corner on line')
	pressToContinue()
	if (l2 == 1):
		break
	else:
		print ('l2 working')
	print('place bL corner on line')
	pressToContinue()
	if (l3 == 1):
		break
	else:
		print ('l3 working')
	print('place br corner on line')
	pressToContinue()
	if (l4 == 1):
		break
	else:
		print ('l4 working')
		
	#Motors
	print('Testing motor now')
	pressToContinue()
	#front
	motors.motor_move('w',4)
	ax, ay, vx, vy, r_mx, r_my = Adafruit_LSM303.mat_accel()
	print('ax = ', ax)
	if (ax < 0 or ax >3000):
		print('ax error')
		break
	print('ay = ', ay)
	if (ay < 0 or ay > 3000):
		print('ay error')
		break
	print('vx = ', vx)
	print('vy = ', vy)
	print('r_mx = ', r_mx)
	print('r_my =', r_my)
	pressToContinue()
	motors.motor_move('x',0)
	#back
	motors.motor_move('s',4)
	time.sleep(3)
	motors.motor_move('x',0)
	#left
	motors.motor_move('a',4)
	print('ax = ', ax)
	if (ax < 0 or ax >3000):
		print('ax error')
		break
	print('ay = ', ay)
	if (ay < 0 or ay > 3000):
		print('ay error')
		break
	print('vx = ', vx)
	print('vy = ', vy)
	print('r_mx = ', r_mx)
	print('r_my =', r_my)
	pressToContinue()
	motors.motor_move('x',0)
	#right
	motors.motor_move('d',4)
	time.sleep(3)
	motors.motor_move('x',0)
	
	
	
	
	
	
	
	
	
		

	
	
