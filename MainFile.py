#! /usr/bin/python

#Accept time input from user
#Calculate difference between,sleep the program
#Turn on the relay
#Turn off the relay

from time import strftime,localtime,sleep
from datetime import datetime
import RPi.GPIO as GPIO

def relayControl():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(2,GPIO.OUT)
  GPIO.output(2,GPIO.HIGH)
  sleep(30)
  GPIO.output(2,GPIO.LOW)
  sleep(5)
  GPIO.cleanup()
 
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
tdelta = diffTimeCalc(alarmTime,sysTime)
tdelta = tdelta.total_seconds()

while True:
  sleep(tdelta)
  startTime = datetime.now().strftime('%H:%M:%S')
  print('Waking up',startTime)
  relayControl()
  endTime=datetime.now().strftime('%H:%M:%S')
  tdelta= diffTimeCalc(startTime,endTime)
  tdelta = 300-(tdelta.total_seconds())

