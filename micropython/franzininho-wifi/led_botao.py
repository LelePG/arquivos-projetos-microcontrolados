from mapeamento import *
from machine import Pin
import time

led = Pin(A_3, Pin.OUT)
btn = Pin(A_6, Pin.IN)

while True:
    if btn.value():
        led.value(1)
        time.sleep(0.2)
        led.value(0)
