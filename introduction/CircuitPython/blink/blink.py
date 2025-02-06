import board
import digitalio
import time

# setup 
led = digitalio.DigitalInOut(board.RED_LED)  # general-purpose RED LED on Pin D3
led.direction = digitalio.Direction.OUTPUT

#init
led.value = False

# main loop
while True:
    led.value = not led.value
    time.sleep(1)
