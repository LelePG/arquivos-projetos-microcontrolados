from mapeamento import *
from time import sleep
from machine import Pin, PWM

lr = PWM(Pin(A_A), freq=5000)
lg = PWM(Pin(A_B), freq=5000)
lb = PWM(Pin(A_C), freq=5000)

def liga_led(r,g,b):
    lr.duty_u16(r)
    lg.duty_u16(g)
    lb.duty_u16(b)

while True:
    liga_led(0,0,16384) 
    sleep(0.25)
    liga_led(16384,0,0)
    sleep(0.25)
    liga_led(0,16384,0)
    sleep(0.25) 