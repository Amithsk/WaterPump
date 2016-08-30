#Program is used to detect water level


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

TRIG =23
ECHO =25

print "System is booting up"

#Init pin
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

state = GPIO.input(ECHO)
print 'The state of ECHO after int',state


#Trigger the sensor
GPIO.output(TRIG,False)
print "Wait for the sensor"

time.sleep(2)



GPIO.output(TRIG,True)
time.sleep(0.00001)
state = GPIO.input(TRIG)
print 'The state of TRIG after int',state


GPIO.output(TRIG,False)

state = GPIO.input(ECHO)
print 'The state of ECHO after Trigger',state

while GPIO.input(ECHO)==0:
  print "Inside the Echo0"
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  print "Inside the Echo1"
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
distance = pulse_duration*17150

distance =round(distance,2)

print "Distance:",distance

GPIO.cleanup()
