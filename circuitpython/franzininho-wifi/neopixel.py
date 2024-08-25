from mapeamento import *
from time import sleep
from neopixel import NeoPixel #adafruit_circuitpython_neopixel

pixel_pin = D_9
num_pixels = 1

pixels = NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


def set_color(color, wait=1):
    pixels.fill(color)
    pixels.show()
    sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    set_color(RED)
    set_color(GREEN)
    set_color(BLUE)
    set_color(YELLOW)
    set_color(CYAN)
    set_color(PURPLE)
