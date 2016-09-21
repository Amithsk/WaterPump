#This file will have
#1/ To check if the file exist
#2/ To write the content into file
#3/ To create the file
#4/ To read the content of the file

import sys
import os
from time import sleep

def isFilePresent():
  print("Inside is file present check")
  try:
      if os.path.isfile('/home/pi/Documents/LED/WaterPump/AlaramTime.py'):
       print ("The file exist")
       return True
      else:
       print ("The file doesn't exist")
       return False
  except:
       print("System error occured during file present check")
       sys.exit(0)


def readFileContent():
  print("Inside read file usecase")
  try:
      file =open("AlaramTime.py",'r')
      AlarmValue=file.readline()
      return(AlarmValue)
  except:
      print("System error during file creation")
      sys.exit(0)

  


def writeFileContent(AlarmValue):
  print("Insde write file usecase")
  try:
      file =open("AlaramTime.py",'w')
      file.write(AlarmValue)
  except:
      print("System error during file creation")
      sys.exit(0)




def createFile():
  print ("Inside create file usecase")
  try:
      file =open("AlaramTime.py",'a')
      file.close()
  except:
      print("System error during file creation")
      sys.exit(0)


def deleteFile():
  print("Inside delete file usecase")
  try:
      os.remove('/home/pi/Documents/LED/WaterPump/AlaramTime.py')
  except:
      print("Error occured during file deletion")
      sys.exit(0)

