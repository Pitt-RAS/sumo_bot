import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

# These two blocks of code configure the PWM settings for
# the two DC motors on the RC car. It defines the two GPIO
# pins used for the input, starts the PWM and sets the
# motors' speed to 0
motor1_in1_pin = 19
motor1_in2_pin = 26
motor2_in1_pin = 6
motor2_in2_pin = 13
motor1= None
motor2= None
class Motors_Class:
	def __init__(self):
	        global motor1_in1_pin
		global motor1_in2_pin
		global motor2_in1_pin
		global motor2_in2_pin
		global motor1
		global motor2
		io.setup(motor1_in1_pin, io.OUT)
		io.setup(motor1_in2_pin, io.OUT)
		io.setup(4,io.OUT)
		motor1 = io.PWM(4,100)
		motor1.start(0)
		motor1.ChangeDutyCycle(0)
		io.setup(17,io.OUT)
		io.setup(motor2_in1_pin, io.OUT)
		io.setup(motor2_in2_pin, io.OUT)
		motor2 = io.PWM(17,100)
		motor2.start(0)
		motor2.ChangeDutyCycle(0)
		io.output(motor1_in1_pin, False)
		io.output(motor1_in2_pin, False)
		io.output(motor2_in1_pin, False)
		io.output(motor2_in2_pin, False)
# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
# This section of code defines the methods used to determine
# whether a motor needs to spin forward osr backwards. The
# different directions are acheived by setting one of the
# GPIO pins to true and the other to false. If the status of
# both pins match, the motor will not turn.
	def motor1_forward(self):
		io.output(motor1_in1_pin, True)
		io.output(motor1_in2_pin, False)

	def motor1_reverse(self):
		io.output(motor1_in1_pin, False)
		io.output(motor1_in2_pin, True)

	def motor2_forward(self):
		io.output(motor2_in1_pin, True)
		io.output(motor2_in2_pin, False)

	def motor2_reverse(self):
		io.output(motor2_in1_pin, False)
		io.output(motor2_in2_pin, True)

# Setting the PWM pins to false so the motors will not move
# until the user presses the first key


# Infinite loop that will not end until the user presses the
# exit key
	def motor_move(self, direction, speednum):
		global motor1_in1_pin
		global motor1_in2_pin
		global motor2_in1_pin
		global motor2_in2_pin
		global motor1
		global motor2
    # Keyboard character retrieval method is called and saved
    # into variable
    # The "x" key will break the loop and exit the program
		char=direction	
	 	if(direction == "x"):
    			#print("Program Ended")
			io.output(motor1_in1_pin, False)
			io.output(motor1_in2_pin, False)
			io.output(motor2_in1_pin, False)
			io.output(motor2_in2_pin, False)
			motor2.ChangeDutyCycle(0)
			motor1.ChangeDutyCycle(0)
		speed = int(speednum)*11
    # The car will drive forward when the "w" key is pressed
		if(char == "w"):
    			self.motor2_forward()
    			motor2.ChangeDutyCycle(speed)
			self.motor1_forward()
			motor1.ChangeDutyCycle(speed)
    # The car will reverse when the "s" key is pressed
		if(char == "s"):
    			self.motor2_reverse()
   			motor2.ChangeDutyCycle(speed)
			self.motor1_reverse()
			motor1.ChangeDutyCycle(speed)
    # The "a" key will toggle the steering left
		if(char == "a"):
        #toggleSteering("left")
			self.motor2_forward()
       			motor2.ChangeDutyCycle(speed)
       			self.motor1_reverse()
       			motor1.ChangeDutyCycle(speed)
    # The "d" key will toggle the steering right
		if(char == "d"):
       			self.motor2_reverse()
       			motor2.ChangeDutyCycle(speed)
       			self.motor1_forward()
       			motor1.ChangeDutyCycle(speed)
    # to save the next key that is pressed
		char = ""

# Program will cease all GPIO activity before terminating
	def motor_clean_up():
		io.cleanup()
