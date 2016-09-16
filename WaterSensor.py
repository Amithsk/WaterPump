#Program is used to detect water level
import RPi.GPIO as GPIO
import time
DANGERLIMIT=16

def waterLevel():
  print "Entering waterlevel usecase"
#Will be used to measure the depth 
  WATERLEVEL= waterLevelCheck()
#Will be used check if water level is fine to trigger motor  
  return (isSafeToTrigger(WATERLEVEL))
  

def waterLevelCheck():
  GPIO.setmode(GPIO.BCM)
  TRIG =24
  ECHO =25

  #Init pin
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_UP)

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
  WATERLEVEL = pulse_duration*17150
  WATERLEVEL =int(round(WATERLEVEL,2))
  print "The water level is",WATERLEVEL
  return WATERLEVEL
  GPIO.cleanup()

def isSafeToTrigger(WATERLEVEL):
  if DANGERLIMIT > WATERLEVEL:
    return True,WATERLEVEL
  else:
     return False
     


