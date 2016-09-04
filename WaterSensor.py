#Program is used to detect water level
import RPi.GPIO as GPIO
import time

def waterLevel():
  print "Entering waterlevel usecase"
  waterLevelCheck()

def waterLevelCheck():
  GPIO.setmode(GPIO.BCM)
  TRIG =23
  ECHO =25

  #Init pin
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


  #Trigger the sensor
  GPIO.output(TRIG,False)
  time.sleep(2)


  #Activate Trigger
  GPIO.output(TRIG,True)
  time.sleep(0.00001)
  GPIO.output(TRIG,False)


  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

#Calculate distance
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration*17150
  distance =round(distance,2)
  print "The water level is",distance
  GPIO.cleanup()
