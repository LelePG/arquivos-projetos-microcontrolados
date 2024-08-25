from mapeamento import *
from machine import Pin
import dht
import time

dht_sensor = dht.DHT11(Pin(A_9))

while True:
    try:
        dht_sensor.measure()
        t = dht_sensor.temperature()
        h = dht_sensor.humidity()
        print(f"Temperatura: {t} °C \t Umidade: {h}%")
    except OSError as e:
        print("Falha na leitura:", e)

    time.sleep(1)
