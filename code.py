# @MTBMaker lab simple blinking light (LED) example 
# Written for Adafruit Trinkent M0 using Circuit Python
# Written against version 7.x 

import time
import board
import digitalio

ledpin = digitalio.DigitalInOut(board.D4)
ledpin.direction = digitalio.Direction.OUTPUT
sleepInterval = 2

while True:
	ledpin.value = True
	time.sleep(sleepInterval)
	ledpin.value = False
	time.sleep(sleepInterval)