#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

ledpin = 11    # define the ledpin
buttonpin = 12 #define the buttonpin

def setup():
	print('Program is starting ....')
	GPIO.setmode(GPIO.BOARD)  #Numbers GPIO's by physical location
	GPIO.setup(ledpin,GPIO.OUT)  # set ledpins mode to output
	GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set buttonpin to input mode, and pull up to high level (3.3V)
	print('using pin%d'%ledpin)


def loop():
	while True:
		if GPIO.input(buttonpin) ==GPIO.HIGH:
			GPIO.output(ledpin, GPIO.HIGH) #led on
			print('... led on')
		else:
			GPIO.output(ledpin,GPIO.LOW)  #led off
			print('... led off')
		



def destroy():
	GPIO.output(ledpin, GPIO.LOW)   #led off
	GPIO.cleanup()	           #release resource


if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt: #When 'ctrl+c' is pressed, the child program destory will be executed
		destroy()