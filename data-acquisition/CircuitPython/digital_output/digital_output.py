import board
import digitalio
import time

actuator = digitalio.DigitalInOut(board.D5) # nRF52840, Grove D2
actuator.direction = digitalio.Direction.OUTPUT

actuator.value = False
while True:
    actuator.value = not actuator.value
    time.sleep(1)
