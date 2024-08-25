from mapeamento import E_2
from time import sleep
import board
from pwmio import PWMOut

TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4

buzzer = PWMOut(E_2, variable_frequency=True)
buzzer.frequency = TONE_FREQ[0]
buzzer.duty_cycle = 2**15  

while True:
    for i in range(len(TONE_FREQ)):
        buzzer.frequency = TONE_FREQ[i]
        sleep(0.5)
    for i in range(len(TONE_FREQ)-1, -1, -1):
        buzzer.frequency = TONE_FREQ[i]
        sleep(0.5)