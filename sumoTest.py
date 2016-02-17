from lineSense2 import lineSensor_Class
from longrangemethod import longrange_Class
from shortrangemethod import shortrange_Class
from minisumo_motorcontrol2 import Motors_Class
from accelerometer import Accel
	
lineSensors= lineSensor_Class()
motors= Motors_Class()
longrange= longrange_Class()
shortrange= shortrange_Class()

short = shortrange.rngsens
longone = longrange.rangesens
# l1 = lineSensors.check1()
# l2 = lineSensors.check2()
# l3 = lineSensors.check3()
l4 = lineSensors.check4()
results = Accel.mag_accel()

# test variables
# l1 = 0
# l2 = 1
# l3 = 1
# l4 = 1

# short = 12
# long = 60
# ax = -4

ax = results[0] 
ay = results[1] 
vx = results[2] 
vy = results[3] 
r_mx = results[4] 
r_my = results[5] 



def pressToContinue():
	command = 0
	while (command != 1):
		command = input('Press 1 to continue: ')
		print(command)
		
#assumes 10mps is max velocity

#Range Sensors
print('\nTESTING SHORT RANGE')
pressToContinue()
print('outside press to continue')
if short < 0 or short > 15: 
	print('\nSHORT RANGE NOT WORKING')
else:
	print('short = ', short)
print('\nTESTING LONG RANGE')
pressToContinue()
if longone < 10 or longone > 80:
	print ('\nLONG RANGE NOT WORKING')
else:
	print('long = ', long)
	
#line sensors
# print('\nTESTING LINE SENSORS')
# pressToContinue()
# print('place left corner over line')
# pressToContinue()
# if (l1 == 1):
	# print('\nL1 NOT WORKING')
# else:
	# print ('l1 working')
# print('\nPlace top right corner on line')
# pressToContinue()
# if (l2 == 1):
	# print('\nL2 NOT WORKING')
# else:
	# print ('l2 working')
# print('place bL corner on line')
# pressToContinue()
# if (l3 == 1):
	# print('\nL3 NOT WORKING')
# else:
	# print ('l3 working')
# print('place br corner on line')
# pressToContinue()
if (l4 == 1):
	print('\nL4 NOT WORKING')
else:
	print ('l4 working')
	
#Motors
print('\nTESTING MOTORS NOW')
pressToContinue()

#FRONT MOTOR TEST
motors.motor_move('w',4)
results = Adafruit_LSM303.mag_accel()
ax = results[0] 
ay = results[1] 
vx = results[2] 
vy = results[3] 
r_mx = results[4] 
r_my = results[5] 
print('ax = ', ax)
if (ax < 0 or ax >.25):
	print('\nAX ERROR')
print('ay = ', ay)
if (ay < 0 or ay > .25):
	print('\nAY ERROR')
print('vx = ', vx)
print('vy = ', vy)
print('r_mx = ', r_mx)
print('r_my =', r_my)
pressToContinue()
motors.motor_move('x',0)

#BACK MOTOR TEST
motors.motor_move('s',4)
print('ax = ', ax)
if (ax < 0 or ax >.25):
	print('\nAX ERROR')
print('ay = ', ay)
if (ay < 0 or ay > .25):
	print('\nAY ERROR')
print('vx = ', vx)
print('vy = ', vy)
print('r_mx = ', r_mx)
print('r_my =', r_my)
pressToContinue()
time.sleep(3)
motors.motor_move('x',0)
	
#LEFT MOTOR TEST
motors.motor_move('a',4)
print('\nAX ERROR')
if (ax < 0 or ax >.25):
	pprint('\nAX ERROR')
print('ay = ', ay)
if (ay < 0 or ay > .25):
	print('\nAY ERROR')
print('vx = ', vx)
print('vy = ', vy)
print('r_mx = ', r_mx)
print('r_my =', r_my)
pressToContinue()
motors.motor_move('x',0)

#RIGHT MOTOR TEST
motors.motor_move('d',4)
if (ax < 0 or ax >.25):
	print('\nAX ERROR')
print('ay = ', ay)
if (ay < 0 or ay > .25):
	print('\nAY ERROR')
print('vx = ', vx)
print('vy = ', vy)
print('r_mx = ', r_mx)
print('r_my =', r_my)
pressToContinue()
time.sleep(3)
motors.motor_move('x',0)

	
	
	
	
	
	
	
		

	
	
