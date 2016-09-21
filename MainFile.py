#! /usr/bin/python

#Accept time input from user
#Calculate difference between,sleep the program
#Turn on the relay
#Turn off the relay

from time import strftime,localtime,sleep
from datetime import datetime,timedelta
import RPi.GPIO as GPIO
from WaterSensor import waterLevel
from Relay import relayTrigger
import FileIO

#Time format
FMT = '%H:%M:%S'

 
def diffTimeCalc(Start,End):
  Diff = datetime.strptime(Start,FMT)-datetime.strptime(End,FMT)
  if Diff.days < 0:
    Diff = timedelta(days=0,seconds=Diff.seconds,microseconds=Diff.microseconds)
  return Diff  

def userInput():

 AlarmTime = input("Please enter the alarm time")
 print("Entered value is",AlarmTime)

 SysTime=datetime.now().strftime('%H:%M:%S')
 print('Systime',SysTime)

 #Calculate the difference
 Tdelta =  diffTimeCalc(AlarmTime,SysTime).total_seconds()
 return Tdelta,AlarmTime


def Main():
#This loop is to check
#1/ Is the program restarted after powerfailure
#2/ Is the program executed for first time
  if (FileIO.isFilePresent()):
    print("Inside file true part")
    AlarmTime = FileIO.readFileContent()
    print("The value of AlarmTime",AlarmTime)
    SysTime=datetime.now().strftime('%H:%M:%S')
    Tdelta =  diffTimeCalc(AlarmTime,SysTime).total_seconds()
    print("The value of Tdelta",Tdelta)
  
  else:
    print("Inside file false part")
    Tdelta,AlarmTime =userInput()
    FileIO.createFile()
    FileIO.writeFileContent(AlarmTime)



  while True:
    try:
        sleep(Tdelta)
        StartTime = datetime.now().strftime('%H:%M:%S')
        print('Waking up',StartTime)
        Indicator,WATERLEVEL =waterLevel()
        if Indicator:
         relayTrigger()
        else:
         print "Water level danger break"
         break
        EndTime=datetime.now().strftime('%H:%M:%S')
        Tdelta = 300-(diffTimeCalc(StartTime,EndTime).total_seconds())
    except KeyboardInterrupt:
         print "The program interrputed"
         FileIO.deleteFile()
         break


Main()
