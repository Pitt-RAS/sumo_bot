import wiringpi2 as wiringpi
import ctypes as ct
import time as ti
io.setmode(io.BCM)
data_pin=27
clock1_pin=22
stat=None
x=None
y=None
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(data_pin,0)
wiringpi.pinMode(data_pin,1)

def gohi(pin):
	wiringpi.pinMode(pin, 0)
	wiringpi.digitalWrite(pin, 1)
def golow(pin):
	wiringpi.pinMode(pin, 1)
	wiringpi.digitalWrite(pin,0)
def write (ct.c_ubyte(data)):
	parity=ct.c_ubyte(1)
	gohi(data_pin)
	gohi(clock1_pin)
	ti.sleep(0.0003)
	golo(clock1_pin)
	ti.sleep(0.0003)
	golo(data_pin)
	ti.sleep(0.00001)
	gohi(clock1_pin)
	while(wiringpi.digitalRead(clock1_pin)==1)
	for i in range(0,8):
		if ((data & 1)==1):
			gohi(data_pin)
		else:
			golo(data_pin)
		while(wiringpi.digitalRead(clock1_pin)==0)
		while(wiringpi.digitalRead(clock1_pin==1)
		a_data= data&1
		parity=parity^a_data
		data=data>>1
	if (parity==1):
		gohi(data_pin)
	else:
		golo(data_pin)
	while(wiringpi.digitalRead(clock1_pin==0)
	while(wiringpi.digitalRead(clock1_pin==1)
	gohi(data_pin)
	ti.sleep(0.00005)
	while(wiringpi.digitalRead(clock1_pin)==1)
	while(wiringpi.digitalRead(clock1_pin)==0 or wiringpi.digitalRead(data_pin)==0) 
	golo(clock1_pin)
def read ():
	data= ct.c_ubyte(0)
	bit=ct.c_ubyte(1)
	gohi(clock1_pin)
	gohi(data_pin)
	ti.sleep(0.00005)
	while(wiringpi.digitalRead(clock1_pin==1)
	ti.sleep(0.000005)
	while(wiringpi.digitalRead(clock1_pin==0)
	for i in range(0,8):
		while(wiringpi.digitalRead(clock1_pin==1)
		if (wiringpi.digitalRead(data_pin)==1):
			data= data | bit
		while(wiringpi.digitalRead(clock1_pin==0)
		bit=bit<<1
	while(wiringpi.digitalRead(clock1_pin==1)
	while(wiringpi.digitalRead(clock1_pin==0)
	while(wiringpi.digitalRead(clock1_pin==1)
	while(wiringpi.digitalRead(clock1_pin==0)
	golo(clock1_pin)
	return data
def mouse_init():
	write(0xFF)
	for i in range(0,3):
		read()
	write(0xF0)
	read();
	ti.sleep(0.0001)
def mouse_pos(stat, x, y):
	pos_data=[]
	write(0xEB)
	read()
	global stat=read()
	global x=read()
	global y=read()
	pos_data.append(stat)
	pos_data.append(x)
	pos_data.append(y)
	return pos_data

dataR= wiringpi.digitalRead(data_pin)
clockR= wiringpi.digitalRead(clock1_pin)
print "Setup"
print clockR
print dataR
mouse_init()
print clockR
print dataR
print "Mouse Ready"

while True:
	global stat=None
	global x=None
	global y=None
	print bin(stat)
	print ("x= ")
	print int(x,2)
	print ("y= ")
	print int(y,2)
	ti.sleep(1)
