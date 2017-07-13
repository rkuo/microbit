# MicroPython
This is a study note that follows [BBC micro:bit MicroPython Documentation Release 0.0.1](https://www-users.cs.york.ac.uk/~mjf/roach/MicroPython/microbit-micropython.pdf). 

[toc]

## Editor

All exercises are mainly based on web-based `mu` IDE, which is different from native local version. 

Difference:

* Web version does not have REPL
* Web version has block construction pane.

Notes:   

Read the feedback section for possible bugs and shortcoming.  
  
* At this version, it looks like one direction only Block -> MicroPython.
* It may be hard to pan design pane (left side of window), by reducing the font size, the bottom of window will be visible for scoll. 
* There is no difference between single and double quotes in Python.
* The first time click the the block menu-button, the block design pane appears, but the script went blank (new program). Quit browser to clear and start a new project.

## Examples

### LED Display Images
Page: 4 (doc) 8 (pdf display)

![displyImage](https://www.evernote.com/l/AS5U10Lm9tJMK6YOGpZiShc6763vlT4TVz0B/image.png)

### Array

Some computer languages use lowercase for the first character of variable name. 

The editor will create *set* and *get* blocks (some OOP language (Object-Oriented Programming), like Java uses the term "method") after you created a variable. The addtional variables created later, can be accessed by using dropdown box in *set* and *get* blocks.  

To rename a variable; 
![rename variable](https://www.evernote.com/l/AS41f_P0e95Jv6vpdV2XaMP9_zcxWQflC9MB/image.png)

To have more than 3 (default) elements in an array;

![add or delete element in an arrary](https://www.evernote.com/l/AS5Yz28r_y1OSY3v9uFbc9VHeWXDxnNZaXgB/image.png)

An array can be displayed inline (horizontal) instead of multiple lines (external inputs, in vertical).

Page: 8 (doc) 12 (pdf display)

`message scroll` will not work, and error message is very hard to read.

This works.
![works](https://www.evernote.com/l/AS7KEZjITDJAf6T_YohoOOSrEPjk5C8Kt2MB/image.png)

Debugging: simply just add one extra character E -> Eg, it does not work anymore. -> possible different types.

![string array does not work](https://www.evernote.com/l/AS7osWxvVM9M-5w9E7X4B6IMTCLfvc1pStIB/image.png) 

![Different objects need different methods](https://www.evernote.com/l/AS6Tv9k0ubtH9ZL6KrXmqfYU7Vc_lNDvIukB/image.png).

![display an array of images](https://www.evernote.com/l/AS62lB2SOvRAypU9QftI2NvfxXUZsqVFYn4B/image.png)

### Animation
Use multiple image to create an array.

![animation](https://www.evernote.com/l/AS5CBCs7OZ5Dp6qKg2DlkeFWNzz5V-f9vWwB/image.png)

`display.show` is for image.

### String 
Page: 10, I could not find the block for `str` conversion function.

### Logic and Loops

Breakout loop in Loops category.
![breakout](https://www.evernote.com/l/AS5Kc618GCdIS4FR7BSdtryv6RMdWzJo5NMB/image.png)

### Sound and Piezo
Page: 15, 
The sound from piezo is not very loud, so I added a display to show the change of states.

![sound and piezo](https://www.evernote.com/l/AS6U9lrFleBNuLBT57NeOkIFw4RNM2mlwy8B/image.png)

### Music

There is some [website selling Microbit compatible speaker](http://microbit-accessories.co.uk/shop/music/mini-speaker/). We can also [experiment the music with a regular headphone](https://www.microbit.co.uk/blocks/lessons/hack-your-headphones/activity). o test wiring, we tried this example.

My experiment;

![wiring for alligator clip to ear butts](https://www.evernote.com/l/AS76Ly76fkVNhY03sV0NfdDl5uY2JOtH9IwB/image.jpg)

[file at google drive can be shared now, just add a ! in front of markdown](https://drive.google.com/uc?id=0B1zRVGPHCi18Y0Y0c2d0NU11dWc)

![test wiring](https://www.evernote.com/l/AS4HML1N7k9MPpC66NrDqn8GZzDDgMgR9mMB/image.png)

It works.

Microbit can play music note; each note is play in the format of `note[octave][:duration]`

Page-18,

![music tunes](https://www.evernote.com/l/AS4wPIyeIf1ObbtAV8QeUAFgpODDCR5GTekB/image.png)

### Random
get a random element from a list elements or a range of numbers.

![random choice](https://www.evernote.com/l/AS7LmvZAmmJDkrJLUfiKEKo_1nSqZIiT3uAB/image.png)

### Gestures
Page-23,

With an Accelerameter, Microbit can detect some orientation of the device: up, down, left, right, face up, face down, freefall, 3g, 6g, 8g, shake.

Even some method return with a String, it may not be inserted it as a parameter for another method. We need to use a variable to serve as middleman. 

<condition> in `if_<condition>_then_else` can accept a String variable.

I do not know the difference between `get_gesture()` to `current_gesture`. This does not work. I do not the reason yet!
![gesture does not work](https://www.evernote.com/l/AS4h4XM-_W9O7qLRJhBwTQKIzKoKfg3ybKkB/image.png)

This works.
![gesture works](https://www.evernote.com/l/AS56pV_MizZBgoWMT-L2i-HCUuaEDpX057kB/image.png)

Because we want the device to react to changing circumstances we use a `while loop`.

### Direction
Page-24,
calibrate() will display on dot in the center at the end of the process.

I could not find `flooring` operator. Try text editor:
![compass](https://www.evernote.com/l/AS4oNlNLY1ZEQqFIp7qJmV9IwrZzsYOyGrkB/image.png)

### Storage

There is a simple file system on the micro:bit, we can use MicroPython access and manipulate this file system, approximately 30k. the file system provided by MicroPython is a flat file system. A flat file system does not have directories - all your files are just stored in the same place.

#### Open file
`mu` editor does not have file system block.






## Warnings

* When an item removed from an array, the slot has been removed, but not item, this leaves the value on script pane.
![possible bug-1 example 2](https://www.evernote.com/l/AS4yoZuJFAJI64ymAxA__wQJe1VyP5vTQvIB/image.png)

* We need to handle Microbit with care, if our hand touchs P0, P1 and p2, which may generate input for the device and trigger the lights on/off.

## Feedback and Open Questions

* how to define a function.
* <condition> in `if_<condition>_then_else` can accept a String variable. This may be a oversight.
* I could not find the block for `str` function.


## Microbit Introduction

* Can be programmed with high-level online IDEs using the BBC's website at http://www.microbit.co.uk/create-code including:
	* Microsoft TouchDevelop IDE
	* Microsoft Blocks
	* CodeKingdoms Javascript
	* MicroPython
	* mbed enabled
		* Online IDE at developer.mbed.org
		* Easy to use C/C++ SDK
		* Dedicated micro:bit runtime libraries for rapid development (developed by Lancaster University)
	* Nordic nRF51822 Multi-protocol Bluetooth® 4.0 low energy/2.4GHz RF SoC
		* 32-bit ARM Cortex M0 processor (16MHz)
		* 16kB RAM
		* 256kB Flash
		* Bluetooth Low Energy Master/Slave capable
* Input/Output
	* 25 LED Matrix
	* Freescale MMA8652 3-axis Accelerometer
	* Freescale MAG3110 3-axis Magnetometer (e-compass)
	* Push Button x2
	* USB and Edge connector Serial I/O
	* 2/3 reconfigurable PWM outputs
	* 5 x Banana/Croc-clip connectors
	* Edge connector
	* 6 x Analog In
	* 6-17 GPIO (configuration dependent)
	* SPI
	* i2c
* USB Micro B connector
* JST power connector (3v)
