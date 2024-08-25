from mapeamento import *
from machine import Pin
import network
import socket
import time

ssid = ''
password = ''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)        

while not wlan.isconnected():
    print('Tentando conectar...')
    time.sleep(1)

#print(f"Meu IP: {wlan.ifconfig()[0]}")
    
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setblocking(0)
s.bind(addr)
s.listen(1)

print('Ouvindo em', addr)

while True:
    if wlan.isconnected():
        try:
            cl, addr = s.accept()
            print('Cliente conectado de', addr)
            request = cl.recv(1024)
            print(request)

            request = str(request)

            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send("Olá do Servidor do MicroPython")
            cl.close()

        except:
            pass
    time.sleep(0.1)