import board
import busio
import digitalio
from adafruit_esp32spi import adafruit_esp32spi

# TODO: Set your Wi-Fi ssid, password
ssid = "MY_SSID"
password = "MY_PASSWORD"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
wifi = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not wifi.is_connected:
    print("\nConnecting...")
    try:
        wifi.connect_AP(ssid, password)
    except RuntimeError as e:
        print("Cannot connect", e)
        continue

print(f"Connected to {wifi.ap_info.ssid}")
print(f"IP address is {wifi.ipv4_address}")
