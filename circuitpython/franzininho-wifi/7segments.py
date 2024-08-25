from mapeamento import *
from digitalio import DigitalInOut, Direction
from time import sleep

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
saidas = [DigitalInOut(x) for x in pinos]

for saida in saidas:
    saida.direction = Direction.OUTPUT

def ligaDisplay(numero):
    representacao = representacaoNumeros[numero]
    for i, saida in enumerate(saidas):
        saida.value = representacao[i]

numero = 0
while True:
    numero = (numero + 1) % 10
    ligaDisplay(numero)
    sleep(1)
