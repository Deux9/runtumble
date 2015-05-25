#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot
from runtumble import *

#INPUT VARIABLES
SIZE=[1000,1000]
START=[0,0]
JACKPOTCENTER=[700,700] #x,y
JACKPOTRADIUS=30
AVGANGLE=68
SRUN=30
LRUN=100
##########################################################################
errors(START,SIZE,JACKPOTCENTER,JACKPOTRADIUS)
STEPS=0
POS=START
COORDS=[[],[]]
while not there(POS,JACKPOTCENTER,JACKPOTRADIUS):
	COORDS[0]=COORDS[0] + [POS[0]]
	COORDS[1]=COORDS[1] + [POS[1]]
	OLDPOS=POS
	STEPS=STEPS + 1
	if closer(POS,OLDPOS,JACKPOTCENTER,JACKPOTRADIUS):
		RUN=LRUN
	else:
		RUN=SRUN
	POS=run(POS,RUN,AVGANGLE)
	
COORDS[0]=COORDS[0] + [POS[0]]
COORDS[1]=COORDS[1] + [POS[1]]
COORDS=[COORDS[0]] + [COORDS[1]]


CIRCLE=circle(JACKPOTCENTER,JACKPOTRADIUS)
print STEPS
matplotlib.pyplot.axis([0,SIZE[0],0,SIZE[1]])
matplotlib.pyplot.plot(COORDS[0],COORDS[1],'b',CIRCLE[0],CIRCLE[1],'r')
matplotlib.pyplot.savefig('myfig')
matplotlib.pyplot.show()

exit




