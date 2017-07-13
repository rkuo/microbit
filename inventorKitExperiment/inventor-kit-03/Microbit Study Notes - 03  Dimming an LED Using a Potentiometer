## Dimming an LED Using a Potentiometer
Inventor's Kit Tutorial

This is to emulate light switch with light level can be set at certain level (by potentiometer in this exercise) when it is turned on, it will be at pre-set level.

[toc]

### Objective and Experiment
* learn to use a push button to turn external LED light on/off
* learn to use potentiometer to set a desired value
* learn to read value from potentiometer and use it to set the brightness of LED

### Parts Used
* potentiometer, for more [details](https://en.wikipedia.org/wiki/Potentiometer)
* resistor 47 ohm
* push switch
* red LED light
* jumper wires

### Schematic Diagram and Breadboard Layout

![wiring diagram for dimming an LED using potentiometer](https://www.evernote.com/l/AS7jLqUEsl9Pw7fOxDWWCNRI1b5ZoGusTKIB/image.jpg)

### Software Components 
We need to
   
* get status of push button, use P0 to store the state 
	* `Make new variable`,
	* `input.on_pin_<P0>_pressed`, 
	* `if_<condition>_then_else`,
	* `set_item_to_<value>`
* read analog value from potentiometer 
	* `analog_read_<P0>`
* send analog value to a component (LED light)
	* `analog_write_<value>_to_<P0>` to write analog
	* `digital_write_<value>_to_pin_<P0>`

### Block Layout and Javascript

1. add a `on pin <P0> pressed` block. This allows us to use a button to interface with P0. We can also add some comment to the block by right click on the block.
![select add comment to a block](https://www.evernote.com/l/AS4vsCuy3BJFnaQiBNvQlIjFO46ovcd_E8YB/image.png)
![comment](https://www.evernote.com/l/AS4FVWH7fgRHdaIQ5LhBAwmm-5Wdfpw_2BMB/image.png) 

2. add a variable `lightState` from Variable category. First click `Make a Variable`, the system will prompt for entering the name. This variable will be available for use later.
![add variable](https://www.evernote.com/l/AS7aFwTL4ExFDoT5bkQQLmZtieiwYSZRJg0B/image.png)

3. add a `if <condition> then-else`. Initially, `<condition>` is set to `true`. If we want to this default value with something else, we need to select from Logic category, like `A = B` or `C and D`; here A and B are value, C and D are logic. 

4. Since we want to track current light state (lightState), which is off at first. If the button connect to P0 is pressed, the system will turn the LED light on and set the current state equal on. 
5. The system should write the value from the potentiometer (P1) to LED (P2)
![blocks](https://www.evernote.com/l/AS4s8557WVZOUa0uXYqgCCEyKtYr_Es56qQB/image.png)
![code](https://www.evernote.com/l/AS4L_6Ny9MdGzLmGwa5Mu8G6yT64bENQ3OoB/image.png) 
The original code only partially works: turn light on and adjust its brightness. It will not be able to turn off. We need add one extra block/statement. 
6. add a `digital write` block.

![add digit write](https://www.evernote.com/l/AS5G37VNO-JFKa294Ld-A6oZhzJZO2uoeL0B/image.png)

```
let lightState = 0
// This block preserves the state of LED light.
input.onPinPressed(TouchPin.P0, () => {
    // toggle lightState On-Off
    if (lightState == 0) {
        lightState = 1
    } else {
        lightState = 0
    }
})
basic.forever(() => {
    if (lightState == 1) {
        pins.analogWritePin(AnalogPin.P2, pins.analogReadPin(AnalogPin.P1))
    } else {
        pins.digitalWritePin(DigitalPin.P2, 0)
        lightState = 0
    }
})
```
Works now.

![working board](https://www.evernote.com/l/AS4wXEKV07ZE0blaPwaKAwaNvYY9TrjZI3gB/image.jpg)

### Discussion
I replaced the potentiometer with the one from Sunfounder's senor kit, it works fine.  
![use sunfounder potentiometer](https://www.evernote.com/l/AS4H4Ei12KxJk7TGrIMgPeqFkGpIleWDNOcB/image.jpg)
