from machine import Pin,SoftI2C
import time
from oled_lib import SSD1306_I2C
from timetable import WEEK

from timer import percent_display


# and 2 dogs


week = WEEK.week


i2c = SoftI2C(scl=Pin(22),sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)






# for i in range(len(texts)):
#     oled.text(texts[i],0, 0)
#     oled.show()
#     time.sleep(2)
#     oled.fill(0)
#     oled.show()



for day in week:
    for period in day.periods:
        oled.fill(0)
        oled.show()
        oled.text(day.day,0,5)
        oled.text(period.name,0,20)
        oled.text(period.venue,0,35)
        oled.show()

        percent_display(period.duration*0.1)

