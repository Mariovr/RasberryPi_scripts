#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

ledpin = 11
def setup():
	GPIO.setmode(GPIO.BOARD)  #Numbers GPIO's by physical location
	GPIO.setup(ledpin,GPIO.OUT)  # set ledpins mode to output
	GPIO.output(ledpin, GPIO.LOW) #set ledpin low to off led
	print('using pin%d'%ledpin)


def loop():
	while True:
		GPIO.output(ledpin, GPIO.HIGH) #led on
		print('... led on')
		time.sleep(1)
		GPIO.output(ledpin,GPIO.LOW)  #led off
		print('... led off')
		time.sleep(0.5)

def destroy():
	GPIO.output(ledpin, GPIO.LOW)   #led off
	GPIO.cleanup()	           #release resource


if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt: #When 'ctrl+c' is pressed, the child program destory will be executed
		destroy()