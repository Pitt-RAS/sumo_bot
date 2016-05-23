from lineSense2 import lineSensor_Class
from longrangemethod import longrange_Class
from shortrangemethod import shortrange_Class
from minisumo_motorcontrol2 import Motors_Class
from minisumo_motorcontrol3 import Motors_Class2
from accelerometer import Accel
import time	
lineSensors= lineSensor_Class()
Accel1 = Accel()
motor1= Motors_Class()
motor2 = Motors_Class2()
longrange= longrange_Class()
shortrange= shortrange_Class()

try:
	while True:
		motor1.motor_move('a', 3)
		motor2.motor_move('a', 3)
		shortrange.rngsens()
		lineSensors.check1()
		lineSensors.check2()
		lineSensors.check3()
		lineSensors.check4()
		longrange.rangesens()
except KeyboardInterrupt:
	GPIO.cleanup()
		
	
