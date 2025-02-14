import board
import chainable_led

pin_clk = board.D9 # nRF52840, Grove D4
pin_data = board.D10 # nRF52840, Grove D5
num_leds = 1
leds = chainable_led.P9813(pin_clk, pin_data, num_leds)
delta = 10

# setup
leds.reset()

# loop
while True:
    print("Fading in...")
    for intensity in range(0, 255, delta):
        leds.fill((0, 0, intensity))
        leds.write()

    print("Fading out...")
    for intensity in range(255, 0, -delta):
        leds.fill((0, 0, intensity))
        leds.write()