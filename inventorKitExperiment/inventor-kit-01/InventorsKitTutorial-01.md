## Say "Hello" to the BBC microbit!
Inventor's Kit Tutorial 01

[toc]

If you have not heard Microbit before or this is the first time you use Microbit, please refer to my [introduction notes](https://goo.gl/iPVX7b) for some general information.  

This is a study notes of Kitronik's Inventor's Kit. Initially, this serves as supplement notes of its booklet. A list of experiement notes at bottom of this page.

### Objective and Experiment
* learn how to use LEDs to display pattern or strings.
* learn how to trigger and observe an event.
* learn how to interface with button on Microbit device.
* learn how to compile a program.
* learn how to load program to a microbit device.

### Parts Used
* 2 buttons
* 4 jump wires
* usb cable to connect to the computer which has internet access. 

There is a good [introduction about push-button](https://www.arduino.cc/en/tutorial/pushbutton) at Arduino site, and from [instructable](http://www.instructables.com/id/Arduino-Button-Tutorial/) about Arduino interfaces with button. Although it is about Arduino, but most of information is usable here. 

**Be in safe side, DON'T use phone charging battery charging block without checking the output voltage. Microbit uses 3.3v**

[Microbit power supply](http://tech.microbit.org/hardware/powersupply/)
[Discussion about power supply at Element 14](https://www.element14.com/community/thread/55711/l/bbc-microbit-battery-power?displayFullThread=true)

### Schematic Diagram and Breadboard Layout

Referring Interface diagram above, P5 is the extended interface for Button-A and P11 is the extended interface for Button-B.  This wiring diagram will create two parallel buttons to the buttons on board, either the button on Microbit board or breadboard will have the same effect. 

Wiring Diagram from Kitronik Inventor's Kit booklet

![01 breadboard and wiring diagram](https://www.evernote.com/l/AS5o-ViLWK5Gk4pzULuJK70-JLm9qRrwSc4B/image.jpg)

Physical Board
![01 breadboard photo](https://www.evernote.com/l/AS4FFEh6eItNWLo3KrqwqkjgoCAp839w20kB/image.jpg)

### Software Components 

(2) input.onButtonPressed  
(1) basic.showLeds  
(1) basic.showString  

The first portion of component is the name of category, which is displayed in the middle of the screen.

### Block Layout

![block layout](https://www.evernote.com/l/AS4_CtnPKDZGErTjXNUr29t_oH_9wbGKq6AB/image.png)

### Javascript

```
basic.forever(() => {
	
})
input.onButtonPressed(Button.A, () => {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, () => {
    basic.showString("Hello World!")
})
```

[Share: download project](https://makecode.microbit.org/_CycPYa2T9i2J)

### Description

* wired two buttons to P4 and P11 each. They are the extensions of two buttons on Microbit. They will not do anything by themselves. 

* wrote a program via block-construction approach, draged the blocks and placed them together. We did not touch `on start` and `forever`, so the block we put in can only run once. 

* Selected different button to identify different button A and B. This allow different behaviors for each button.

* modified `Hello` string to `Hello World` to demo different message can be sent.

* clicked stop (square button) or run (triangle button) on the stage pane. The system runs by default.

You can save the program to cloud or download to your computer or device (plug in your Microbit to USB port of your computer). 

For Mac, this will show a icon on your desktop with name "MICROBIT" as below.

![MICROBIT icon on desktop](https://www.evernote.com/l/AS7C9laKBFhDJJU3zkXyIwEnfvArwnebl10B/image.png)

For Window, 
Microbit is treated as USB storage devices, you can view the content from file directory.

![External USB device](https://www.evernote.com/l/AS7owkaVU4FN7ZwDSbfZIM9thCplCvGxhoUB/image.png)

If you downloaded to different place (file directory), you can just drag <projectfile>.hex file to Microbit device.

![drag to device](https://www.evernote.com/l/AS7oFfWsfIRJupbS4Srj0-0JrE_ImEQU3f8B/image.png)

After you download it to your device, the device will run your program with battery power as above. 

### Learning Microbit
* [Microbit Study Notes - 00 Get Started](https://goo.gl/iPVX7b)
* [Microbit Study Notes - 01 Say "Hello" to the BBC microbit!](https://goo.gl/ft4lFD)  
* [Microbit Study Notes - 02 Using Light Dependent Resistor (LDR) and Analog Inputs]()  
* [Microbit Study Notes - 03 Dimming an LED Using a Potentionmeter]()  
