## Wind Power
Inventor's Kit Tutorial

[toc]

### Objective and Experiment  

* learn to generate voltage by blowing a fan
* learn to measure voltage by using analog input from a pin

Using the motor and fan in experiment 04, but reverse the wiring to generate voltage when we will blow on the attached fan.

### Parts Used  
* two 2.2k ohm resistors
* one motor with fan

### Schematic Diagram and Breadboard Layout
![wiring diagram](https://www.evernote.com/l/AS4_YssVns1HqL6CS0zO42ZR55n4Z52MMEcB/image.jpg)

### Software Components 
* two `var` to record currentReading and highestValue.
* `pins -> analog read pin(P0)` to get reading.
* `if_<condition>_then_else` to decide whether we got higher voltage or not.
* `input -> on_button_pressed(A)_do` to display the measurement.

### TouchDevelop Script
![script](https://www.evernote.com/l/AS51sO7BQR1FPbA6a8oJmwPbQa9BXWRRglgB/image.png)

### Discussion

I could not make it work! Investigate this later, learn how to debug.



