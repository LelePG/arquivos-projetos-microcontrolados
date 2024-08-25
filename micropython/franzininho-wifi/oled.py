from mapeamento import *
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

largura = 128
altura = 64
i2c = I2C(sda=Pin(C_0), scl=Pin(C_1))
display = SSD1306_I2C(largura, altura, i2c)

while True:
    display.text('Hello, World!', 0, 0, 1)
    display.show()
    sleep(2)

    display.fill(0)
    display.show()
    sleep(2)

    display.pixel(10,10,1) 
    display.show()
    sleep(2)

    # escrever texto, pode ser necessário https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/main/examples/font5x8.bin
    display.text('Hello', 0, 0,1) # texto, x, y, cor_pixel
    display.text('World', 0, 10,1) # texto, x, y, cor_pixel
    display.show()
    sleep(2)

    display.invert(1)
    display.show()
    sleep(2)

    display.invert(0)
    display.show()
    sleep(2)