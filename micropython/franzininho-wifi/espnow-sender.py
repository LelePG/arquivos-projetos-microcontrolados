from mapeamento import *
import espnow
import network
import espnow
from machine import Pin, ADC
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

mac_address = wlan.config('mac')
print('Endereço MAC:', ':'.join(['{:02x}'.format(b) for b in mac_address]))

esp = espnow.ESPNow()
esp.active(True)
peer = b'\x34\xb4\x72\x6c\x60\xaa' 
esp.add_peer(peer) 

pot = ADC(B_8)
btn = Pin(A_5, Pin.IN)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    if btn.value():
        valor = f'{map(pot.read(), 0,8191,0,1023)}'
        esp.send(peer,valor) # None como 1 param para enviar para todos os peers
        print(f'mandando {valor}')
    time.sleep(0.5)
    
   

