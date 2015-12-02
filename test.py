import time
from lineSense2 import check1
from lineSense2 import check2
from lineSense2 import check3
from lineSense2 import check4
from minisumo_motorcontrol2 import motormove
from longrangemethod import rangesens
from shortrangemethod import rngsens

motormove('w', 4)

while(True):
	if(1==check1()):
		motormove('x')
		time.sleep(1)
		motormove('s',4)
	elif(1==check2()):
		motormove('x')
		time.sleep(1)
		motormove('s',4)
	elif(1==check3()):
		motormove('x')
		time.sleep(1)
		motormove('s',4)
	elif(1==check4()):
		motormove('x')
		time.sleep(1)
		motormove('s',4)
	elif(rngsens()<3):
		motormove('x')
		time.sleep(1)
		motormove('w',4)
	elif(rngsens()<20):
		motormove('x')
		time.sleep(1)
		motormove('w',4)
