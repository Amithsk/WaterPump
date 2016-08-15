#! /usr/bin/python

#Accept time input from user
#Calculate difference between User input time and Sys time
#Sleep the program
#Wake up after the sleep duration
#light up the LED in specific pattern

from time import strftime,localtime,sleep
from datetime  import datetime
#from gpiozero import LED
#led =LED(15)
FMT = '%H:%M:%S'

alarmTime =input("Please enter the alarm time")
print ("Entered values is",alarmTime)

sysTime=datetime.now().strftime('%H:%M:%S')
print('Systime',sysTime)

tdelta =datetime.strptime(alarmTime,FMT)-datetime.strptime(sysTime,FMT)
tdelta = tdelta.total_seconds()
print("Sys  millisecond",tdelta)

while True:
  sleep(tdelta)
  startTime= datetime.now().strftime('%H:%M:%S')
  print('Waking up',startTime)
  sleep(10)
  endTime=datetime.now().strftime('%H:%M:%S')
  tdelta=datetime.strptime(endTime,FMT)-datetime.strptime(startTime,FMT)
  tdelta = 60-(tdelta.total_seconds())

#led.on()
#sleep(10)
#led.off()
