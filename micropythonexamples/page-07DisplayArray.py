from microbit import *


shoppingList = ['Eggs', 'Bacons', 'Tomatoes']
while True:
  if button_a.was_pressed():
    display.show(shoppingList)
