import time
import adafruit_dht
import board

# Constants
INTERVAL = 5

# Setup
dht = adafruit_dht.DHT11(board.D9)  # nRF52840, Grove D4
    
# Main Loop
while True:
    start = time.time()
    t = time.localtime(start)
    try:
        # Read the temperature and convert it to integer
        temperature = int(round(dht.temperature))
        # Read the humidity and convert it to integer
        humidity = int(round(dht.humidity))
        # Print timestamp, temperatur, humidity
        print(f"{t.tm_hour:d}:{t.tm_min:02d}:{t.tm_sec:02d},{temperature:0.1f},{humidity:0.1f}")
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print(f"{t.tm_hour:d}:{t.tm_min:02d}:{t.tm_sec:02d},-1,-1")
    end = time.time()
    # Wait for the remaining time
    time.sleep(INTERVAL - (end - start))