from mapeamento import A_3, A_6
from digitalio import DigitalInOut, Direction
from time import sleep

led = DigitalInOut(A_3)
led.direction = Direction.OUTPUT
btn = DigitalInOut(A_6)
btn.direction = Direction.INPUT

while True:
    if btn.value:
        led.value = True
        sleep(0.2)
        led.value = False
