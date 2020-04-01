import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

if GPIO.input(4):
	print "HIGH SIGNAL RECIEVED"
	print "LED on"
	GPIO.output(23,GPIO.HIGH)
	time.sleep(5)
	print "LED off"
	GPIO.output(23,GPIO.LOW)