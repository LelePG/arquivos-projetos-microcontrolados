from mapeamento import *
from machine import Pin
from keypad import Keypad
from time import sleep

cols = [Pin(x) for x in (E_6,E_5,E_4,E_3)]
rows = [Pin(x) for x in (D_A, D_B, D_C, D_D)]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']]

keypad = Keypad(rows, cols, keys)

while True:
    key_pressed = keypad.read_keypad()
    if key_pressed:
        print("Key pressed:", key_pressed)
    sleep(0.1)  