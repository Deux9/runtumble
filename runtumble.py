#!/usr/bin/env python
import math
import numpy
import operator

#INPUT VARIABLES
SIZE=[1000,1000]
START=[0,0]
JACKPOTCENTER=[500,500] #x,y
JACKPOTRADIUS=50
AVGANGLE=68
SRUN=30
LRUN=100
def makeangle(deg):
	return float(deg) / 180 * math.pi
	
def tumble(AVGANGLE):
	return numpy.random.normal(makeangle(AVGANGLE),math.pi)
	
def run(STARTPOS,RUNL,AVGANGLE):
	ANGLE=tumble(AVGANGLE)
	LENGTH=numpy.random.normal(RUNL,RUNL)
	RUN=[LENGTH*math.sin(ANGLE),LENGTH*math.cos(ANGLE)]
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

def closer(POS,OLDPOS,JACKPOTCENTER,JACKPOTRADIUS):
	POSDIF=map(operator.sub,JACKPOTCENTER,POS)
	POSDIFL=math.sqrt(POSDIF[0] ** 2 + POSDIF[1] ** 2)
	OLDPOSDIF=map(operator.sub,JACKPOTCENTER,OLDPOS)
	OLDPOSDIFL=math.sqrt(OLDPOSDIF[0] ** 2 + OLDPOSDIF[1] ** 2)
	return POSDIFL<OLDPOSDIFL

def errors(START,SIZE,JACKPOTCENTER,JACKPOTRADIUS):
	for i in range (0,1):
		if START[i]>SIZE[i] or JACKPOTCENTER[i]>SIZE[i]:
			print "increase SIZE"
		
def circle(JACKPOTCENTER,JACKPOTRADIUS):
	CIRCLE=[[],[]]
	for i in range (0,360):
		CIRCANGLE=makeangle(i)
		CIRCLE[0]=CIRCLE[0] + [JACKPOTCENTER[0] + (JACKPOTRADIUS * math.sin(CIRCANGLE))]
		CIRCLE[1]=CIRCLE[1] + [JACKPOTCENTER[1] + (JACKPOTRADIUS * math.cos(CIRCANGLE))]
	return CIRCLE

def getsteps():
	return STEPS
