## Using Light Dependent Resistor (LDR) and Analog Inputs
Inventor's Kit Tutorial

Light Dependent Resistor (LDR) is a sensor whose resistance is effected by the light. The more light shines on it, the less the resistance of the sensor. Microbit can measure the variation of the resistance by combining with a resistor inline.   

[toc]

### Objective and Experiment
* learn how to LDR as a sensor
* learn how to read analog value for P0
* learn how to set threshold for an analog input and trigger an action when it passes the threshold.

### Parts Used
* LDR (Light Dependency Resistor)
* 10k resistor
* Microbit + USB cable

### Schematic Diagram and Breadboard Layout

![schematic diagram LDR](https://www.evernote.com/l/AS5p4Yo2pzVIj7Fk0Iyx0fGDP-io_bQAZtkB/image.jpg)

### Software Components 
basic.forever
variables.setItemTo
logic.if-<condition>-then-else
logic.compareAEqualB
basic.showLEDs

### Block Layout and Javascript

1. add `variables.setItemTo` block to `forever` and rename (click the down arrow) the item to `light`.  

![add setItemTo](https://www.evernote.com/l/AS5bXt6-aF1AV5mK17HhzP3-plqYn5VAU7UB/image.png)

This creates the Javascript as below. It defines a variable `light` and initialize its value equal 0. When we use it in forever loop, `light` is set to `0`.

```
let light = 0
basic.forever(() => {
    light = 0
})
```

2. open Advance to expand the additional categories, to access Pins catagory, drag a `analog read pin-P0 behind to (on top of 0)`

![get analog reading for P0](https://www.evernote.com/l/AS7DigGEZTlF9KP7_uPN5sAjRh6wgYbklQAB/image.png)

The system translates the block to Javascript as below:
light value equals the analog value we get from pin P0.

Analog value is a continous value we get from physical world, like wind speed, temperature, blood pressure. It gets digitalized by the system; this board can convert our measured voltage to 0 (min) to 1027 (max). It  does matter what we are measure at P0. In this example, we measure ambient light.

```
let light = 0
basic.forever(() => {
    light = pins.analogReadPin(AnalogPin.P0)
})
```

3. add a `if-then-else` block from Logic category. Our plan is to tell computer to one thing, if the light level is at certain value and do something else if the light level is below certain value. If the condition is true, it will do the first block of (then) code, if it is false, it will do else code. The current block is true all the time, we need to add/replace it to a different block, which can be true or false at different time. 

![add if-then-else](https://www.evernote.com/l/AS7-eK6swMJJJrp1iu-tU_6Pm2FpxZEmw8MB/image.png)

4. drag a `logic.compareValueOfAB` on top of `true` block, and change `=` (equal sign) to `>` (greater sign). 

![add compareAB](https://www.evernote.com/l/AS7OYrWH4BNBr7Vi37EifzJmQS6easJqw9oB/image.png)

5. add `light` block to replace the first `0` in the comparison block. (Since we renamed a generic `item` to `light`, which is available in the Variable category now. 

![select light variable](https://www.evernote.com/l/AS5TKaj5g-9EqJobSk7RUICa_Lb5J1Wv5WIB/image.png)

6. change the second `0` to 512. You should have block constructed like below:

![](https://www.evernote.com/l/AS5b6KacjFBH5I-nScM_84b2i2ywIAijNjYB/image.png)

and Javascript code as below:

```
let light = 0
basic.forever(() => {
    light = pins.analogReadPin(AnalogPin.P0)
    if (light > 512) {
    	
    } else {
    	
    }
})
```
We have not define what the system should do at either conditions (true or false).

7. add two `basic.showLEDs` and model the patterns like sun and moom, see bolow.

![show sun or moon](https://www.evernote.com/l/AS71AQqcaZZCFptNi25aFr6gvR33ILI9d6sB/image.png)

8. run the program and click the P0 on the simulation board, which will randomly value and triggers different LED pattern. This is a good way to test your program without wire the physical device.

![run the program](https://www.evernote.com/l/AS5A-HZdBNRPaY5AJLJmVTwYbioG1bMdoTkB/image.png)

9. wire physical parts together as described above. check your wiring before you plug in USB cable. 

10. download program to Microbit and test it with a flash light.

![run program on device](https://www.evernote.com/l/AS6CXyx5o_BEA7hiRLD-GBxF90UL_4NjKhwB/image.png)

[Share: download project](https://pxt.microbit.org/_RMbXR8iwTUip)

### Description
The more light on LDR, the less its resistance it has, then the more voltage drop at R1. This pushes more voltage at P0 too. 

The right-hand side of the picture above shows there is a flash light shining on LDR, which gives higher value from LDR sensor. Since it is higher than the threshold, the LED shows a pattern like sun.

### Learning Microbit
* [Microbit Study Notes - 00 Get Started](https://goo.gl/iPVX7b)
* [Microbit Study Notes - 01 Say "Hello" to the BBC microbit!](https://goo.gl/ft4lFD)  
* [Microbit Study Notes - 02 Using Light Dependent Resistor (LDR) and Analog Inputs]()  
* [Microbit Study Notes - 03 Dimming an LED Using a Potentionmeter]()  



