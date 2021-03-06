#!/usr/bin/python

# Python library for Adafruit Flora Accelerometer/Compass Sensor (LSM303).
# This is pretty much a direct port of the current Arduino library and is
# similarly incomplete (e.g. no orientation value returned from read()
# method).  This does add optional high resolution mode to accelerometer
# though.

# Copyright 2013 Adafruit Industries

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

#<<<<<<< HEAD:accelerometer.py
#=======
from Adafruit_I2C import Adafruit_I2C

#>>>>>>> origin/master:sumobot/accelerometer.py
class Adafruit_LSM303(Adafruit_I2C):

    # Minimal constants carried over from Arduino library
    LSM303_ADDRESS_ACCEL = (0x32 >> 1)  # 0011001x
    LSM303_ADDRESS_MAG   = (0x3C >> 1)  # 0011110x
                                             # Default    Type
    LSM303_REGISTER_ACCEL_CTRL_REG1_A = 0x20 # 00000111   rw
    LSM303_REGISTER_ACCEL_CTRL_REG4_A = 0x23 # 00000000   rw
    LSM303_REGISTER_ACCEL_OUT_X_L_A   = 0x28
    LSM303_REGISTER_MAG_CRB_REG_M     = 0x01
    LSM303_REGISTER_MAG_MR_REG_M      = 0x02
    LSM303_REGISTER_MAG_OUT_X_H_M     = 0x03

    # Gain settings for setMagGain()
    LSM303_MAGGAIN_1_3 = 0x20 # +/- 1.3
    LSM303_MAGGAIN_1_9 = 0x40 # +/- 1.9
    LSM303_MAGGAIN_2_5 = 0x60 # +/- 2.5
    LSM303_MAGGAIN_4_0 = 0x80 # +/- 4.0
    LSM303_MAGGAIN_4_7 = 0xA0 # +/- 4.7
    LSM303_MAGGAIN_5_6 = 0xC0 # +/- 5.6
    LSM303_MAGGAIN_8_1 = 0xE0 # +/- 8.1


    def __init__(self, busnum=-1, debug=False, hires=False):

        # Accelerometer and magnetometer are at different I2C
        # addresses, so invoke a separate I2C instance for each
        self.accel = Adafruit_I2C(self.LSM303_ADDRESS_ACCEL, busnum, debug)
        self.mag   = Adafruit_I2C(self.LSM303_ADDRESS_MAG  , busnum, debug)

        # Enable the accelerometer
        self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27)
        # Select hi-res (12-bit) or low-res (10-bit) output mode.
        # Low-res mode uses less power and sustains a higher update rate,
        # output is padded to compatible 12-bit units.
        if hires:
            self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A,
              0b00001000)
        else:
            self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0)
  
        # Enable the magnetometer
        self.mag.write8(self.LSM303_REGISTER_MAG_MR_REG_M, 0x00)


    # Interpret signed 12-bit acceleration component from list
    def accel12(self, list, idx):
        n = list[idx] | (list[idx+1] << 8) # Low, high bytes
        if n > 32767: n -= 65536           # 2's complement signed
        return n >> 4                      # 12-bit resolution


    # Interpret signed 16-bit magnetometer component from list
    def mag16(self, list, idx):
        n = (list[idx] << 8) | list[idx+1]   # High, low bytes
        return n if n < 32768 else n - 65536 # 2's complement signed


    def read(self):
        # Read the accelerometer
        list = self.accel.readList(
          self.LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80, 6)
        res = [( self.accel12(list, 0),
                 self.accel12(list, 2),
                 self.accel12(list, 4) )]
	global x
	global y
	x = (self.accel12(list,0))/9.8
	y = (self.accel12(list,4))/9.8

        # Read the magnetometer
        list = self.mag.readList(self.LSM303_REGISTER_MAG_OUT_X_H_M, 6)
        res.append((self.mag16(list, 0),
                    self.mag16(list, 2),
                    self.mag16(list, 4),
                    0.0 )) # ToDo: Calculate orientation

    def setMagGain(gain=LSM303_MAGGAIN_1_3):
        self.mag.write8( LSM303_REGISTER_MAG_CRB_REG_M, gain)
    def get_x(self):
	global x
	return x
    def get_y(self):
	global y
	return y

#Simple example prints accel/mag data once per second:
# if __name__ == '__main__':

    # from time import sleep

    # lsm = Adafruit_LSM303()

    # print '[(Accelerometer X, Y, Z), (Magnetometer X, Y, Z, orientation)]'
    # while True:
        # print lsm.read()
        # sleep(1) # Output is fun to watch if this is commented out
	def get_x():
		global x
		return x
	def get_y():
		global y
		return y	


class Accel (Adafruit_LSM303):
	def mag_accel(self, x0, y0):
		from time import sleep
		lsm = Adafruit_LSM303()

		print '[(Accelerometer X, Y, Z), (Magnetometer X, Y, Z, orientation)]'
		axtotal = aytotal = mxtotal = mytotal = 0
		for i in xrange(1,5):
			lsm.read()
			axfirst = lsm.get_x()
			ayfirst = lsm.get_y()
			#print "Acceleration x: %d" % (axfirst)
			#print "Accleration y: %d" % (ayfirst)
			data= [axfirst, ayfirst]
			return data
			sleep(.05)
            #READ VALUES FROM ACCELEROMETER AND MAGNETOMETER
			# newOut = lsm.read()

			# mx = newOut[3]
			# my = newOut[4]
			# mx1 = mx - mxlast
			# my1 = my - mylast
			# mxtotal = mxtotal + mx1
			# mytotal = mytotal + my1
			
			# ax= newOut[0]
			# ay = newOut[1]

			# ax1 = ax-axlast
			# ay1 = ay-aylast
			# axtotal = axtotal + ax1
			# aytotal = aytotal + ay1

			#get velocity
			r_mx = int(mxtotal/5)
			r_my = int(mytotal/5)
			r_ax = int(axtotal/5)
			r_ay = int(aytotal/5)
			vx = int(r_ax*(.25))
			vy = int(r_ay*(.25))
			
			print "Velocity x: %d" % (vx)
			print "Velocity y: %d" % (vy)

            # SMOOTHING
       		dt = .05
           	RC = 0.3
            	alpha = dt / (RC + dt)
            	smooth_x = (alpha * axfirst) + (1 - alpha) * x0
            	smooth_y = (alpha * ayfirst) + (1 - alpha) * y0
		data= [smooth_x, smooth_y, x0, y0]
		#return data
			
			# print "Mag x: %d" % (r_mx)
			# print "Mag y: %d" % (r_my)
            # return_array[0] = axtotal
            # return_array[1] = aytotal
            # return_array[2] = vx
            # return_array[3] = vy







			  
# sleep(1) # Output is fun to watch if this is commented out



