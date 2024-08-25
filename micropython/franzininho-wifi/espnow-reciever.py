import network
import espnow
from machine import Pin, PWM
import time

led = PWM(Pin(1), freq=5000)  

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
esp = espnow.ESPNow()
esp.active(True)

mac_address = wlan.config('mac')
#print('Endereço MAC:', ':'.join(['{:02x}'.format(b) for b in mac_address]))

while True:
    host, msg = esp.recv()
    if msg:
        dado = int(msg.decode('utf-8'))
        led.duty(dado) 




