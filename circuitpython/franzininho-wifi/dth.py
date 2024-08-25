from mapeamento import *
from time import sleep
import adafruit_dht #adafruit_circuitpython_dht

dht = adafruit_dht.DHT11(A_9)

while True:
    try:
        t = dht.temperature
        h = dht.humidity
        print(f"Temperatura: {t} *C \t Umidade: {h}%")
    except RuntimeError as e:
        print("Falha na leitura: ", e.args)

    sleep(1)
