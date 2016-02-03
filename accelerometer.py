# Simple example prints accel/mag data once per second:
from Adafruit_LSM303 import Adafruit_LSM303
class Accel (Adafruit_LSM303):
	def mag_accel():
		from time import sleep
		lsm = Adafruit_LSM303()
	
		print '[(Accelerometer X, Y, Z), (Magnetometer X, Y, Z, orientation)]'
		axtotal = aytotal = mxtotal = mytotal = 0
		for i in xrange(1,5):
			output = lsm.read()
			axlast = output[0]
			aylast = output[1]
			azlast = output[2]
			mxlast = output[3]
			mylast = output[4]
			mzlast = output[5]
			ax1 = ay1 = mx1 = my1 = 0
			
			sleep(.05)
			newOut = lsm.read()
			mx = newOut[3]
			my = newOut[4]
			mx1 = mx - mxlast
			my1 = my - mylast
			mxtotal = mxtotal + mx1
			mytotal = mytotal + my1
			
			ax= newOut[0]
			ay = newOut[1]
			ax1 = ax-axlast
			ay1 = ay-aylast
			axtotal = axtotal + ax1
			aytotal = aytotal + ay1
			
			r_mx = int(mxtotal/5)
			r_my = int(mytotal/5)
			r_ax = int(axtotal/5)
			r_ay = int(aytotal/5)
			vx = int(r_ax*(.25))
			vy = int(r_ay*(.25))
			
			print "Velocity x: %d" % (vx)
			print "Velocity y: %d" % (vy)
			print "Mag x: %d" % (r_mx)
			print "Mag y: %d" % (r_my)  
		return (axtotal, aytotal, vx, vy, r_mx, r_my)
			  
# sleep(1) # Output is fun to watch if this is commented out



