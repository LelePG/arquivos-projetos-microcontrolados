from mapeamento import *
import espnow
from time import sleep
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

e = espnow.ESPNow()
peer = espnow.Peer(mac=b'4\xb4rl`\xaa')
e.peers.append(peer)   
        
pot = AnalogIn(B_8)
btn = DigitalInOut(A_5)
btn.direction = Direction.INPUT

while True:
    if btn.value:
        valor = f'{pot.value}'
        e.send(valor) 
        print(f'mandando {valor}')
    sleep(0.5)
