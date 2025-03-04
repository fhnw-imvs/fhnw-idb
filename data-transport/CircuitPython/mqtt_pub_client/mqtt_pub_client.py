import board
import busio
import digitalio
import time
import adafruit_connection_manager
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

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

# MQTT setup
mqtt_broker = "test.mosquitto.org"
mqtt_topic = "hello"

def handle_connect(client, userdata, flags, rc):
    print("Connected to {0}".format(client.broker))

def handle_publish(client, userdata, topic, pid):
    print("Published to {0} with PID {1}".format(topic, pid))

# Set callback handlers
mqtt_client = MQTT.MQTT(
    broker=mqtt_broker,
    socket_pool=adafruit_connection_manager.get_radio_socketpool(wifi)
)

mqtt_client.on_connect = handle_connect
mqtt_client.on_message = handle_publish

print("Attempting to connect to %s" % mqtt_client.broker)
mqtt_client.connect()

while True:
    t = int(time.monotonic())
    mqtt_message = "Hello, up for {0}s".format(t)
    mqtt_client.publish(mqtt_topic, mqtt_message)
    time.sleep(5)