#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

#Set 8 Pins for 8 leds:
#LedPins = [17,18,27,22,23,24,25,4]
LedPins = [17,27]
buttonpin = 18 #define the buttonpin

#Define a function to print a message at the beginning.
def print_message():
    print('Program is running ....')
    print('Please press ctrl-C to end the program')
    input('Press Enter to begin\n')

#Define a setup for some function.
def setup():
    #Numbers GPIO's by BCM numbering.
	GPIO.setmode(GPIO.BCM)  
	GPIO.setup(LedPins,GPIO.OUT,initial=GPIO.LOW)  # set ledpins mode to output
	GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set buttonpin to input mode, and pull up to high level (3.3V)

def loop():
    print('Press button to start &stop')
    while True:
        if GPIO.input(buttonpin) ==GPIO.HIGH:
            main()
            time.sleep(5)
        else:
            pass

def main():
    #print messages
    #print_message()
    leds =['-','-']
    while True:
        #Turn LED on from left to right.
        for pin in LedPins:
                    GPIO.output(pin, GPIO.HIGH) #led on
                    leds[LedPins.index(pin)] = '0'
                    print(leds)
                    time.sleep(0.5)
                    GPIO.output(pin,GPIO.LOW)  #led off
                    leds[LedPins.index(pin)] = '-'

        #Turn LED on from right to left.
        for pin in LedPins:
                    GPIO.output(pin, GPIO.HIGH) #led on
                    leds[LedPins.index(pin)] = '0'
                    print(leds)
                    time.sleep(0.5)
                    GPIO.output(pin,GPIO.LOW)  #led off
                    leds[LedPins.index(pin)] = '-'
        if GPIO.input(buttonpin) ==GPIO.HIGH:
            break
		



def destroy():
    #Turn off all LEDS.
	GPIO.output(LedPins, GPIO.HIGH)   #leds off
	GPIO.cleanup()	           #release resource


if __name__ == '__main__':
	setup()
	try:
		loop()
    #when ctrl-c is pressed the child program destroy() will be executed.
	except KeyboardInterrupt: #When 'ctrl+c' is pressed, the child program destory will be executed
		destroy()
