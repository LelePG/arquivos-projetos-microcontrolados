from mapeamento import *
from time import sleep
import pwmio

lr = pwmio.PWMOut(A_A, frequency=5000, duty_cycle=0)
lg = pwmio.PWMOut(A_B, frequency=5000, duty_cycle=0)
lb = pwmio.PWMOut(A_C, frequency=5000, duty_cycle=0)

def liga_led(r,g,b):
    lr.duty_cycle = r
    lg.duty_cycle = g
    lb.duty_cycle = b

while True:
    liga_led(0,0,16384) 
    sleep(0.25)
    liga_led(16384,0,0)
    sleep(0.25)
    liga_led(0,16384,0)
    sleep(0.25) 