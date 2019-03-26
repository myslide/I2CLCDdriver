import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

#use: lcd_display_string("the text", linenumber)
mylcd.lcd_display_string("Hello World!", 1)
