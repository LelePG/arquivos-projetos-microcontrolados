from mapeamento import *
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from machine import ADC, PWM, Pin
import time

pot_x = ADC(Pin(B_1))
pot_y = ADC(Pin(B_0))

largura = 128
altura = 64
i2c = I2C(sda=Pin(C_0), scl=Pin(C_1))
display = SSD1306_I2C(largura, altura, i2c)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    x_mapeado = map(pot_x.read_u16(),0,65535,0,largura-1)
    y_mapeado = map(pot_y.read_u16(),0,65535,0,altura-1)
    display.fill(0)
    display.pixel(x_mapeado, y_mapeado, 1)
    display.show()
    sleep(0.25)

