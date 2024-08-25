import busio # pacote com funcionalidades de i2c, spi e uart
import adafruit_ssd1306 # adafruit_circuitpython_ssd1306
from mapeamento import *
from analogio import AnalogIn
from time import sleep
from math import trunc

pot_x = AnalogIn(B_1)
pot_y = AnalogIn(B_0)

def map(x, in_min, in_max,out_min,out_max):
  return trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min);

largura = 128
altura = 64

SDA = C_0
SCL = C_1
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(largura, altura, i2c)


while True:
    x_mapeado = map(pot_x.value,0,51375,0,largura)
    y_mapeado = map(pot_y.value,0,51375,0,altura)
    oled.fill(0)
    oled.pixel(x_mapeado, y_mapeado, 1)
    oled.show()
    sleep(0.25)               