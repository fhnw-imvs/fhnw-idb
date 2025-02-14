import board
import time
from ultrasonic_ranger import Ultrasonic

_ULTRASONIC_SENSOR = board.D9 # nRF5840 D9, Grove D4

sonar = Ultrasonic(_ULTRASONIC_SENSOR)

while True:
    dist = sonar.measure_in_centimeters()
    print(dist)
    time.sleep(1)