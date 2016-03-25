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
l1 = lineSensors.check1()
# l2 = lineSensors.check2()
# l3 = lineSensors.check3()
l4 = lineSensors.check4()

x0 = 0
y0 = 0
#DRIVE FORWARD TEST LOOP
while True:
	motors.motor_move('w', 4)
	if l1 == 1: #if senses front line sensor.
		motors.motor_move('x', 0)
		break
	if short > 0 and short < 15:
		print('short = ', short)
		motors.motor_move('x', 0)
		time.sleep(2)
		motor.motor_move('w', 4)
	if long > 10 and long < 80:
		print('long = ', long)
		motors.motor_move('x', 0)
		time.sleep(2)
		motor.motor_move('w', 4)
    ax, ay, x0, y0 = Accel.mag_accel(x0, y0)
	print ('acceleration: ', ax0, '\t', ay0)

# DRIVE BACKWARD TEST
while True:
	if l4 == 1:
		motors.motor_move('x', 0)
		break
    if short > 0 and short < 15:
        print('short = ', short)
        motors.motor_move('x', 0)
        time.sleep(2)
        motor.motor_move('s', 4)
    if long > 10 and long < 80:
        print('long = ', long)
        motors.motor_move('x', 0)
        time.sleep(2)
        motor.motor_move('s', 4)
    ax, ay, x0, y0 = Accel.mag_accel(x0, y0)
    print ('acceleration: ', ax, '\t', ay)












# OLD CODE
# def pressToContinue():
# 	command = 0
# 	while (command != 1):
# 		command = input('Press 1 to continue: ')
# 		print(command)
#
# #assumes 10mps is max velocity
#
# #Range Sensors
# print('\nTESTING SHORT RANGE')
# pressToContinue()
# print('outside press to continue')
# if short < 0 or short > 15:
# 	print('\nSHORT RANGE NOT WORKING')
# else:
# 	print('short = ', short)
# print('\nTESTING LONG RANGE')
# pressToContinue()
# if longone < 10 or longone > 80:
# 	print ('\nLONG RANGE NOT WORKING')
# else:
# 	print('long = ', long)
#
# #line sensors
# # print('\nTESTING LINE SENSORS')
# # pressToContinue()
# # print('place left corner over line')
# # pressToContinue()
# # if (l1 == 1):
# 	# print('\nL1 NOT WORKING')
# # else:
# 	# print ('l1 working')
# # print('\nPlace top right corner on line')
# # pressToContinue()
# # if (l2 == 1):
# 	# print('\nL2 NOT WORKING')
# # else:
# 	# print ('l2 working')
# # print('place bL corner on line')
# # pressToContinue()
# # if (l3 == 1):
# 	# print('\nL3 NOT WORKING')
# # else:
# 	# print ('l3 working')
# # print('place br corner on line')
# # pressToContinue()
# if (l4 == 1):
# 	print('\nL4 NOT WORKING')
# else:
# 	print ('l4 working')
#
# #Motors
# print('\nTESTING MOTORS NOW')
# pressToContinue()
#
# #FRONT MOTOR TEST
# motors.motor_move('w',4)
# x0 = 0
# y0 = 0
# [x0, y0] = Adafruit_LSM303.mag_accel(x0, y0)
# print('ax = ', ax)
# if (ax < 0 or ax >.25):
# 	print('\nAX ERROR')
# print('ay = ', ay)
# if (ay < 0 or ay > .25):
# 	print('\nAY ERROR')
# print('vx = ', vx)
# print('vy = ', vy)
# print('r_mx = ', r_mx)
# print('r_my =', r_my)
# pressToContinue()
# motors.motor_move('x',0)
#
# #BACK MOTOR TEST
# motors.motor_move('s',4)
# print('ax = ', ax)
# if (ax < 0 or ax >.25):
# 	print('\nAX ERROR')
# print('ay = ', ay)
# if (ay < 0 or ay > .25):
# 	print('\nAY ERROR')
# print('vx = ', vx)
# print('vy = ', vy)
# print('r_mx = ', r_mx)
# print('r_my =', r_my)
# pressToContinue()
# time.sleep(3)
# motors.motor_move('x',0)
#
# #LEFT MOTOR TEST
# motors.motor_move('a',4)
# print('\nAX ERROR')
# if (ax < 0 or ax >.25):
# 	pprint('\nAX ERROR')
# print('ay = ', ay)
# if (ay < 0 or ay > .25):
# 	print('\nAY ERROR')
# print('vx = ', vx)
# print('vy = ', vy)
# print('r_mx = ', r_mx)
# print('r_my =', r_my)
# pressToContinue()
# motors.motor_move('x',0)
#
# #RIGHT MOTOR TEST
# motors.motor_move('d',4)
# if (ax < 0 or ax >.25):
# 	print('\nAX ERROR')
# print('ay = ', ay)
# if (ay < 0 or ay > .25):
# 	print('\nAY ERROR')
# print('vx = ', vx)
# print('vy = ', vy)
# print('r_mx = ', r_mx)
# print('r_my =', r_my)
# pressToContinue()
# time.sleep(3)
# motors.motor_move('x',0)

	
	
	
	
	
