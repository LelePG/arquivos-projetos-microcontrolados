from mapeamento import *
import keypad
from digitalio import DigitalInOut
import adafruit_matrixkeypad # adafruit_circuitpython_matrixkeypad
from time import sleep

cols = [DigitalInOut(x) for x in (E_6,E_5,E_4,E_3)]
rows = [DigitalInOut(x) for x in (D_A, D_B, D_C, D_D)]
keys = ((1, 2, 3, "A"), (4, 5, 6, "B"), (7, 8, 9, "C"), ("*", 0, "#", "D"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    sleep(0.1)
