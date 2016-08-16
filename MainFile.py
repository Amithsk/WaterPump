#! /usr/bin/python

#Accept time input from user
#Calculate difference between,sleep the program
#Turn on the relay
#Turn off the relay

from time import strftime,localtime,sleep
from datetime import datetime
import RPI.GPIO as GPIO

#Configure Relay
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

#Time format
FMT = '%H:%M:%S'

alaramTime = input("Please enter the alarm time")
print("Entered value is",alaramTime)

sysTime=datetime.now().strftime('%H:%M:%S')
print('Systime',sysTime)

#Calculate the difference
tdelta = datetime.strptime(alarmTime,FMT)-datetime.strptime(sysTime,FMT)
tdelta = tdelta.total_seconds()

while True:
  sleep(tdelta)
  startTime = datetime.now().strftime('%H;%M:%S')
  print('Waking up',startTime)
  GPIO.output(2,GPIO.HIGH)
  sleep(30)
  GPIO.output(2,GPIO.LOW)
  GPIO.cleanup()
  endTime=datetime.now().strftime('%H:%M:%S')
  tdelta=datetime.strptime(endTime,FMT)-datetime.strptime(startTime,FMT))
  tdelta = 300-(tdelta.total_seconds())

