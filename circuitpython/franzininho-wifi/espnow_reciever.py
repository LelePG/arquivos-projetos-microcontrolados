from mapeamento import *
from analogio import AnalogIn
import espnow
import pwmio

e = espnow.ESPNow()
led = pwmio.PWMOut(A_0, frequency=5000, duty_cycle=0)

while True:
    if e:
        packet = e.read()
        dado = packet.msg.decode('utf-8')
        print(f'recebendo {dado}')
        led.duty_cycle = int(dado)