from mapeamento import B_1, A_3
from time import sleep
from analogio import AnalogIn, AnalogOut
import pwmio

#Importante, o AnalogIn funciona em qualquer pino com ADC, e o AnalogOut só funciona em pinos com DAC
pot = AnalogIn(B_1)
led = pwmio.PWMOut(A_3, frequency=5000, duty_cycle=0)

while True:
    print((pot.value,)) 
    led.duty_cycle = pot.value
    sleep(0.25)               
    
