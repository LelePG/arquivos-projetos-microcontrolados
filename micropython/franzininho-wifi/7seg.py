from mapeamento import *
from machine import Pin
import time

representacaoNumeros = [
    [1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 0, 0, 0, 0], 
    [1, 1, 0, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0, 0, 1], 
    [0, 1, 1, 0, 0, 1, 1], 
    [1, 0, 1, 1, 0, 1, 1], 
    [1, 0, 1, 1, 1, 1, 1], 
    [1, 1, 1, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 0, 1, 1]
]

pinos = [D_0, D_1, D_2, D_3, D_4, D_5, D_6]
saidas = [Pin(x, Pin.OUT) for x in pinos]

def ligaDisplay(numero):
    representacao = representacaoNumeros[numero]
    for i, saida in enumerate(saidas):
        saida.value(representacao[i])

numero = 0
while True:
    numero = (numero + 1) % 10
    ligaDisplay(numero)
    time.sleep(1)
