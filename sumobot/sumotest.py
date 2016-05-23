from lineSense2 import lineSensor_Class
from longrangemethod import longrange_Class
from shortrangemethod import shortrange_Class
from minisumo_motorcontrol2 import Motors_Class
from minisumo_motorcontrol3 import Motors_Class2
from accelerometer import Accel
import time
import RPi.GPIO as GPIO	
lineSensors= lineSensor_Class()
Accel1 = Accel()
motor1= Motors_Class()
motor2 = Motors_Class2()
longrange= longrange_Class()
shortrange= shortrange_Class()

#create file

def moving(dir):
	if dir == 'x':
		motor1.motor_move('x', 0)
		motor2.motor_move('x', 0)
	if dir == 'a':
		motor1.motor_move('a', 5)
		motor2.motor_move('a',5)
	if dir == 's':
		motor1.motor_move('s',8)
		motor2.motor_move('s',8)
	if dir == 'd':
		motor1.motor_move('d', 5)
		motor2.motor_move('d', 5)
	if dir == 'w':
		motor1.motor_move('w',8)
		motor2.motor_move('w', 8)
try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21,GPIO.IN)
	while(True):
		if(GPIO.input(21)==False):
			time.sleep(5)
			break;
	x0 = 0
	y0 = 0
	press = 'w'
	moving(press)
	shortrange.rngsens()
        longrange.rangesens()
	while True:
		shortrange.rngsens()
        	longrange.rangesens()
		if(lineSensors.check1()==1):
			press='s'
			counter = 0
			while(lineSensors.check4()==0):
			        longrange.rangesens()
				if (counter == 7):
                                        break
				moving(press)
			press = 's'
			moving(press)
                if(lineSensors.check3()==1):
			press='s'
			counter= 0
                        while(lineSensors.check2()==0):
			        longrange.rangesens()
				if (counter == 7):
                                        break
                                moving(press)
                        press = 's'
                        moving(press)
                if(lineSensors.check2()==1):
			press='a'
			counter = 0
                        while(lineSensors.check4()==0):
			        longrange.rangesens()
				if (counter == 7):
                                        break
                                counter=counter +1
                		longrange.rangesens()
                                moving(press)
                        press = 'w'
                        moving(press)
          	if(lineSensors.check4()==1):
			press='d'
			counter= 0
                        while(lineSensors.check2()==0):
				if (counter == 7):
					break
				counter=counter +1
                		longrange.rangesens()
                                moving(press)
                        press = 'w'
                        moving(press)
		shortrange.rngsens()
	        longrange.rangesens()
except KeyboardInterrupt:
	motor1.motor_clean_up()
	motor2.motor_clean_up()		
	

	
	
	
	
	
