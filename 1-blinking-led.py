from gpiozero import LED
from time import sleep

led = LED(25)

slow_delay = 1
fast_delay = 0.1
delay = slow_delay

def flip_delay(delay):
    if delay == slow_delay:
        delay = fast_delay
    else:
        delay = slow_delay
    return delay

while True:
    led.on()
    print('LED set to on')
    sleep(delay)
    led.off()
    print('LED set to off')
    sleep(delay)
    delay = flip_delay(delay)
