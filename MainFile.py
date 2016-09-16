#! /usr/bin/python

#Accept time input from user
#Calculate difference between,sleep the program
#Turn on the relay
#Turn off the relay

from time import strftime,localtime,sleep
from datetime import datetime
import RPi.GPIO as GPIO
from WaterSensor import waterLevel
from Relay import relayTrigger

 
def diffTimeCalc(start,end):
  diff = datetime.strptime(start,FMT)-datetime.strptime(end,FMT)
  return diff  

#Time format
FMT = '%H:%M:%S'

alarmTime = input("Please enter the alarm time")
print("Entered value is",alarmTime)

sysTime=datetime.now().strftime('%H:%M:%S')
print('Systime',sysTime)

#Calculate the difference
tdelta =  diffTimeCalc(alarmTime,sysTime).total_seconds()

while True:
  sleep(tdelta)
  startTime = datetime.now().strftime('%H:%M:%S')
  print('Waking up',startTime)
  Indicator,WATERLEVEL =waterLevel()
  if Indicator:
    relayTrigger()
  else:
    print "Water level danger break"
    break
  endTime=datetime.now().strftime('%H:%M:%S')
  tdelta = 300-(diffTimeCalc(alarmTime,sysTime).total_seconds())

