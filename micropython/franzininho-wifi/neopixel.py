from machine import Pin
from neopixel import NeoPixel
from time import sleep
from mapeamento import *

pixel_pin = Pin(D_9, Pin.OUT)
num_pixels = 1

pixels = NeoPixel(pixel_pin, num_pixels)

def set_color(color, wait=1):
    pixels.fill(color)
    pixels.write()
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
