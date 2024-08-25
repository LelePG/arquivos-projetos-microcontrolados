from mapeamento import A_3
import digitalio
import time

led = digitalio.DigitalInOut(A_3)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)