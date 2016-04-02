from minisumo_motorcontrol2 import Motors_Class
from minisumo_motorcontrol3 import Motors_Class2

motors=Motors_Class()
motors2=Motors_Class2()
while(1):
	direct = raw_input()
	motors.motor_move(direct,4)
        motors2.motor_move(direct,4)
