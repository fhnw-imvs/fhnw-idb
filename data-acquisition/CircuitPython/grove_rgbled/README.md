# Controlling a Chainable RGB LED
How to control the *Chainable RGB LED* with CircuitPython.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the "library" file [chainable_led.py](chainable_led.py) to the _CIRCUITPY_ drive.
* Copy the content of [test_led.py](test_led.py) to _code.py_ on the _CIRCUITPY_ drive.

## Library
* There seems to be no official Chainable RGB LED CircuitPython library from Adafruit yet.

## Hardware
* [Feather nRF52840 Express](https://github.com/fhnw-imvs/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [Grove shield for Feather](https://github.com/fhnw-imvs/fhnw-idb/wiki/Grove-Adapters#grove-shield-for-feather) to connect sensors.
* [Chainable RGB LED](https://github.com/fhnw-imvs/fhnw-idb/wiki/Grove-Actuators#chainable-rgb-led) wired to Grove _D4_ (nRF52840 _D9_ and _D10_).
