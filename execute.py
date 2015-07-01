#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot
import runtumble

#INPUT VARIABLES
SIZE=[1000,1000]
START=[700,300]
JACKPOTCENTER=[500,500] #x,y
JACKPOTRADIUS=30
AVGANGLE=62
SRUN=50
LRUN=70

##########################################################################
#check for errors
runtumble.errors(START,SIZE,JACKPOTCENTER,JACKPOTRADIUS)

#initialize variables
STEPS=0
POS=START
COORDS=[[],[]]
OLDPOS=POS
ANGLE=AVGANGLE

while not runtumble.there(POS,JACKPOTCENTER,JACKPOTRADIUS):
	COORDS[0]=COORDS[0] + [POS[0]]
	COORDS[1]=COORDS[1] + [POS[1]]
	STEPS=STEPS + 1
	if runtumble.closer(POS,OLDPOS,JACKPOTCENTER):
		LENGTH=LRUN
	else:
		LENGTH=SRUN
	OLDPOS=POS
	ANGLE=ANGLE+runtumble.tumble(AVGANGLE)
	POS=runtumble.run(POS,LENGTH,ANGLE,SIZE)
	
COORDS[0]=COORDS[0] + [POS[0]]
COORDS[1]=COORDS[1] + [POS[1]]
COORDS=[COORDS[0]] + [COORDS[1]]


CIRCLE=runtumble.circle(JACKPOTCENTER,JACKPOTRADIUS)
print STEPS
matplotlib.pyplot.axis([0,SIZE[0],0,SIZE[1]])
matplotlib.pyplot.plot(COORDS[0],COORDS[1],'b',CIRCLE[0],CIRCLE[1],'r')
matplotlib.pyplot.savefig('myfig')
matplotlib.pyplot.show()

exit




