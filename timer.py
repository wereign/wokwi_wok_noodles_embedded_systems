from machine import Pin
from neopixel import NeoPixel
import time
num_led = 16
np = NeoPixel(Pin(23),num_led)


def percent_display(given_time_in_mins):
  # the delay time in seconds
  # follows the logic that

  mins = given_time_in_mins/10
  print("Time of increment:",mins,"minutes")
  for i in range(0,10):
    np[i] = (200,0,0)
    np.write()
    
    # * 60 here to convert to seconds
  time.sleep(mins*60)

  for i in range(0,10):
    np[i] = (0,255,0)
    np.write()
    print(i+1,'% done!')
    time.sleep(mins*60)


