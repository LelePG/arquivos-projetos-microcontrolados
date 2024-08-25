from mapeamento import *
from machine import ADC, PWM, Pin
import time

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

pot = ADC(Pin(B_8))
led = PWM(Pin(A_3), freq=5000)

while True:
    pot_value = map(pot.read(), 0,8191,0,1023)
    led.duty(pot_value) # o valor precisa estar entre 0 e 1023
    time.sleep(0.25)
