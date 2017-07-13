from microbit import *


while True:
  display.show(Image.HEART)
  pin0.write_digital(1)
  sleep(20)
  display.show(Image.SAD)
  pin0.write_digital(0)
  sleep(480)
