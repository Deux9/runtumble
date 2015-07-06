#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot
import runtumble

#INPUT VARIABLES
SIZE=[1000,1000]
START=[500,500]
AVGANGLE=62
LENGTH=50
REPEAT=500
##########################################################################
#initialize variables
STEPS=0
POS=START
COORDS=[[],[]]
OLDPOS=POS
ANGLE=AVGANGLE

for i in range(0,REPEAT):
	COORDS[0]=COORDS[0] + [POS[0]]
	COORDS[1]=COORDS[1] + [POS[1]]
	OLDPOS=POS
	ANGLE=ANGLE+runtumble.tumble(AVGANGLE)
	POS=runtumble.run(POS,LENGTH,ANGLE,SIZE)
	
COORDS[0]=COORDS[0] + [POS[0]]
COORDS[1]=COORDS[1] + [POS[1]]
COORDS=[COORDS[0]] + [COORDS[1]]


matplotlib.pyplot.axis([0,SIZE[0],0,SIZE[1]])
matplotlib.pyplot.plot(COORDS[0],COORDS[1],'b')
matplotlib.pyplot.savefig('random')
matplotlib.pyplot.show()

exit




