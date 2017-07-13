from microbit import *


aCurrentGesture = accelerometer.get_gestures()

if aCurrentGesture == 'face up':
  display.show(Image.HAPPY)
else:
  display.show(Image.SAD)
