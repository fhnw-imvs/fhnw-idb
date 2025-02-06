import board
import digitalio
import time
import sys

# setup
led = digitalio.DigitalInOut(board.D5)  # Pi Zero W, Grove D5
led.direction = digitalio.Direction.OUTPUT

# init
led.value = False

# main loop
try:
    while True:
        led.value = not led.value
        time.sleep(0.5)
except KeyboardInterrupt:
    led.value = False
    sys.exit(0)
