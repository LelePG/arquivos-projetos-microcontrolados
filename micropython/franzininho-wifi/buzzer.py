from mapeamento import *
from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(E_2))

TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4


buzzer.freq(TONE_FREQ[0])

while True:
    for i in range(len(TONE_FREQ)):
        buzzer.freq(TONE_FREQ[i])
        sleep(0.5)
    for i in range(len(TONE_FREQ)-1, -1, -1):
        buzzer.freq(TONE_FREQ[i])
        sleep(0.5)