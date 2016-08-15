import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)


GPIO.output(2,GPIO.HIGH)
sleep(90)
GPIO.output(2,GPIO.LOW)
sleep(5)
GPIO.cleanup()
