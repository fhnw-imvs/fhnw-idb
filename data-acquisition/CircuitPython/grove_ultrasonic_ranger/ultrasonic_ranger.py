import time
import digitalio

class Ultrasonic:
    def __init__(self, pin):
        self.pin = pin
        self.data = digitalio.DigitalInOut(pin)

    def pulse_in(self, pin, state, timeout=1000000000):
        start_time = time.monotonic_ns()

        # Wait for any previous pulse to end
        while pin.value == state:
            if time.monotonic_ns() - start_time >= timeout:
                return 0
        # Wait for the pulse to start
        while pin.value != state:
            if time.monotonic_ns() - start_time >= timeout:
                return 0

        pulse_start = time.monotonic_ns()

        # Wait for the pulse to stop
        while pin.value == state:
            if time.monotonic_ns() - start_time >= timeout:
                return 0

        pulse_end = time.monotonic_ns()

        # Convert time difference to microseconds
        return (pulse_end - pulse_start)/1000.0


    def duration(self):
        self.data.direction = digitalio.Direction.OUTPUT
        self.data.value = False
        time.sleep(0.000002)  # 2 microseconds
        self.data.value = True
        time.sleep(0.000005)  # 5 microseconds
        self.data.value = False
        self.data.direction = digitalio.Direction.INPUT

        pulse_duration = self.pulse_in(self.data, True)
        return pulse_duration

    def measure_in_centimeters(self):
        return round(self.duration() / 29 / 2, 1)

    def measure_in_millimeters(self):
        return round(self.duration() * (10 / 2) / 29, 1)
