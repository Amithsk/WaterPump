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

def waterLevel():
  GPIO.setmode(GPIO.BCM)
  TRIG = 23
  ECHO = 25

#Init pin  
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Trigger the sensor
  GPIO.output(TRIG,False)
  time.sleep(2)
  GPIO.output(TRIG,True)
  time.sleep(0.00001)
  GPIO.output(TRIG,False)
#Policing the state if ECHO
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
   
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
  pulse_duration = pulse_end =pulse_start
  distance = pulse_duration*17150
  distance = round(distance,2)
  print "Distance",distance
  GPIO.cleanup()

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
  waterLevel()
  endTime=datetime.now().strftime('%H:%M:%S')
  tdelta= diffTimeCalc(startTime,endTime)
  tdelta = 300-(tdelta.total_seconds())

