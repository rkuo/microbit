from microbit import *


while True:
  if button_a.is_pressed():
    display.show(Image.HEART)
  elif button_b.is_pressed():
    break
  else:
    display.show(Image.SAD)
