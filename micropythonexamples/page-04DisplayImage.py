from microbit import *


while True:
  if accelerometer.was_gesture("shake"):
    display.show(Image.HAPPY)
    sleep(1000)
    display.clear()
