from mapeamento import A_3, A_6, E_2
from digitalio import DigitalInOut, Direction
from time import sleep
from simpleio import tone #adafruit_circuitpython_simpleio

led = DigitalInOut(A_3)
led.direction = Direction.OUTPUT
btn = DigitalInOut(A_6)
btn.direction = Direction.INPUT

while True:
    if btn.value:
        led.value = True
        sleep(0.2)
        led.value = False
        tone(E_2, 355, 0.25)
