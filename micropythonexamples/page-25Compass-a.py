from microbit import *

compass.calibrate()
while True:
  needle = (((15 - compass.heading()) - 64 % 10) / 30) % 12

display.show(Image.ALL_CLOCKS[needle])
