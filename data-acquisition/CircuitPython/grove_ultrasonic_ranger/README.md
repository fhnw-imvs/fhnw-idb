# Controlling a Chainable RGB LED
How to control the *Chainable RGB LED* with CircuitPython.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the "library" file [ultrasonic_ranger.py](ultrasonic_ranger.py) to the _CIRCUITPY_ drive.
* Copy the content of [test_ultrasonic.py](test_ultrasonic.py) to _code.py_ on the _CIRCUITPY_ drive.

## Library
* There seems to be no official Chainable RGB LED CircuitPython library from Adafruit yet.

## Hardware
* [Feather nRF52840 Express](https://github.com/fhnw-imvs/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [Grove shield for Feather](https://github.com/fhnw-imvs/fhnw-idb/wiki/Grove-Adapters#grove-shield-for-feather) to connect sensors.
* [Ultrasonic Ranger](https://github.com/fhnw-imvs/fhnw-idb/wiki/Grove-Sensors#ultrasonic-ranger) wired to Grove _D4_ (nRF52840 _D9_).
