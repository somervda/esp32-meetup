
#Result: Blink

import time
from machine import Pin

led = Pin(2, Pin.OUT)  # Define led pin as output

for x in range(5):
    led.value(1)  # light on led
    print("on:", x)
    time.sleep(0.5)
    led.value(0)  # light off led
    time.sleep(0.5)
    print("off:", x)
