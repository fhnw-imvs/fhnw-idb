import board
import busio
import digitalio
from adafruit_esp32spi import adafruit_esp32spi # :)

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
wifi = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while True:
    print("\nScanning...")
    networks = wifi.scan_networks()
    for network in networks:
        print(f"rssi: {network.rssi}, ssid: {network.ssid}")
