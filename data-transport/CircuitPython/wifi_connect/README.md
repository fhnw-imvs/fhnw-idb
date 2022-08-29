# Connecting to a Wi-Fi network
How to connect to a local Wi-Fi network with the FeatherWing ESP32 AirLift Wi-Fi module.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Set your Wi-Fi _ssid_ and _password_ in the [wifi_connect.py](wifi_connect.py) example.
* Copy the content of [wifi_connect.py](wifi_connect.py) to _code.py_ on the _CIRCUITPY_ drive.

## Libraries
From the [CircuitPython libraries](https://circuitpython.org/libraries) bundle:
* Copy _lib/adafruit_esp32spi/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/) and [docs](https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/index.html)).
* Copy _lib/adafruit_bus_device/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/) and [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html)).

## Hardware
* [Feather nRF52840 Express](https://github.com/fhnw-imvs/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing ESP32 AirLift](https://github.com/fhnw-imvs/fhnw-idb/wiki/FeatherWing-ESP32-AirLift) Wi-Fi module.

## Credits
* Based on https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/tree/master/examples licensed under MIT License
