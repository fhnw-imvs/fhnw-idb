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
        print(f"{t.tm_hour:d}:{t.tm_min:02d}:{t.tm_sec:02d},{temperature:0.1f},{humidity:0.1f}")
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print(f"{t.tm_hour:d}:{t.tm_min:02d}:{t.tm_sec:02d},-1,-1")
    end = time.time()
    # Wait for the remaining time
    time.sleep(INTERVAL - (end - start))