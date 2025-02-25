import time
import adafruit_sht4x
import board

# Constants
INTERVAL = 5

# Setup
i2c = board.I2C()  # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
    
# Main Loop
while True:
    start = time.time()
    t = time.localtime(start)
    try:
        temperature, humidity = sht.measurements
        # Print timestamp, temperatur, humidity
        print("{:d}:{:02d}:{:02d},{:g},{:g}".format(
            t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity))

    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("{:d}:{:02d}:{:02d},{:g},{:g}".format(
            t.tm_hour, t.tm_min, t.tm_sec, -1, -1))

    end = time.time()
    # Wait for the remaining time
    time.sleep(INTERVAL - (end - start))
