#!/usr/bin/env python
import math
import numpy
import operator
import random

def tumble(AVGANGLE):
	RESULT=float(random.sample([-1,1],1)[0]) * float(numpy.random.rayleigh(numpy.radians(AVGANGLE) , math.pi)[0])#maybe use gamma dist?
	return RESULT
	
def run(STARTPOS,RUNL,ANGLE,SIZE):
	LENGTH=numpy.random.triangular(0,0,RUNL)
	#LENGTH=numpy.random.normal(RUNL,RUNL - 20)
	RUN=[LENGTH * math.cos(ANGLE),LENGTH * math.sin(ANGLE)]
	POS=map(operator.add,STARTPOS,RUN)
	#for i in range (0,1):
	#	if POS[i]<0:
	#		POS[i]=0
	#	if POS[i]>SIZE[i]:
	#		POS[i]=SIZE[i]
	if POS[0]<0:
		POS[0]=0
	if POS[1]<0:
		POS[1]=0
	if POS[0]>SIZE[0]:
		POS[0]=SIZE[0]
	if POS[1]>SIZE[1]:
		POS[1]=SIZE[1]
	return POS

def there(POS,JACKPOTCENTER,JACKPOTRADIUS):
	POSDIF=map(operator.sub,JACKPOTCENTER,POS)
	POSDIFL=math.sqrt(POSDIF[0] ** 2 + POSDIF[1] ** 2)
	return POSDIFL<=JACKPOTRADIUS

def closer(POS,OLDPOS,JACKPOTCENTER):
	POSDIF=map(operator.sub,JACKPOTCENTER,POS)
	POSDIFL=math.sqrt((POSDIF[0] ** 2) + (POSDIF[1] ** 2))
	OLDPOSDIF=map(operator.sub,JACKPOTCENTER,OLDPOS)
	OLDPOSDIFL=math.sqrt((OLDPOSDIF[0] ** 2) + (OLDPOSDIF[1] ** 2))
	return POSDIFL<OLDPOSDIFL

def errors(START,SIZE,JACKPOTCENTER,JACKPOTRADIUS):
	for i in range (0,1):
		if START[i]>SIZE[i] or JACKPOTCENTER[i]>SIZE[i]:
			print "increase SIZE"
		
def circle(JACKPOTCENTER,JACKPOTRADIUS):
	CIRCLE=[[],[]]
	for i in range (0,360):
		CIRCANGLE=numpy.radians(i)
		CIRCLE[0]=CIRCLE[0] + [JACKPOTCENTER[0] + (JACKPOTRADIUS * math.cos(CIRCANGLE))]
		CIRCLE[1]=CIRCLE[1] + [JACKPOTCENTER[1] + (JACKPOTRADIUS * math.sin(CIRCANGLE))]
	return CIRCLE

def getsteps():
	return STEPS
