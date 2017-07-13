## Using the Accelerometer to Control Motor Speed
Inventor's Kit Tutorial

[toc]

### Objective and Experiment

* learn what is Accelerometer and how it work
* learn how to use an accelerometer to control fan motor speed.

### Parts Used  

**Same as experiment 04**  

* built-in Acceleromter on Microbit board

### Schematic Diagram and Breadboard Layout

**Same as experiment 04**   
![wiring diagram](https://www.evernote.com/l/AS5rfqQ61xNJBZ5jMi0IvGHgTQk7iiqRflAB/image.png)

This is very interesting concept, all hardware is the same, including interface <P0>, as previous example, only the software changed. accelerometer(y) is available all the time from Microbit. 

### Software Components 

* make variable
* pin -> analog write `<value>` to `<P0>`

### Block Layout and Javascript

Accelerometer can generate wider range of value, to make sure the input value is between Min/Max (0/1023) [clamp function](https://legacy.touchdevelop.com/docs/mathclamp) is used.  

![code](https://www.evernote.com/l/AS6S3NpF6BxKb4-PRqOJb2l0fGs2YCZgZZkB/image.png)

### Discussion
* It will not work, if it is layed flat on the table, it needs to be tipped.

* Interface port `<P0>`, `<P1>`, and `<P2>` can be input or output, the meaning is determined by the application, for example, value = 200, can be duty or roll. How is 200 will be interpreted is up to application. 

![](https://www.evernote.com/l/AS7eKth5SXdPKZhO9U9ObmloInBqk7dzK8sB/image.jpg)

