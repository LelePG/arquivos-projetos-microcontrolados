import busio # pacote com funcionalidades de i2c, spi e uart
import adafruit_ssd1306 # adafruit_circuitpython_ssd1306
from mapeamento import *

largura = 128
altura = 64

SDA = C_0
SCL = C_1
i2c = busio.I2C(SCL, SDA)

oled = adafruit_ssd1306.SSD1306_I2C(largura, altura, i2c)

# encher a tela
#oled.fill(0) # preenche a tela com desligando e 1 ligando
#oled.show()

# controlar os pixels, com as coordenadas x, y e 0 ou 1 pra dizer se vai ligar ou desligar pixel
#oled.pixel(0, 0, 1) # x, y, cor_pixel
#oled.show()

# escrever texto, pode ser necessário https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/main/examples/font5x8.bin
#oled.fill(0)
#oled.text('Hello', 0, 0,1) # texto, x, y, cor_pixel
#oled.text('World', 0, 10,1) # texto, x, y, cor_pixel
#oled.show()

#inverter oled
#oled.invert(False)
