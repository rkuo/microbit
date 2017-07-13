## Using Transistor to Drive a Motor
Inventor's Kit Tutorial

[toc]

### Objective and Experiment
* learn to use transistor to drive motor.
* learn to use Pulse Width Modulation (PWM) to control motor speed.

The system will increase the motor speed to maximun then decrease the speed.  

### Parts Used
We will use one transistor to control the motor speed. 
	* Transistor: the middle leg serves as a gate or power. 

Read more [details transistor here](https://en.wikipedia.org/wiki/Transistor)

### Schematic Diagram and Breadboard Layout

![wiring diagram](https://www.evernote.com/l/AS7Kvugdr_RETaNH7FYgBsw5lX3FAxh0m6YB/image.jpg)
The middle leg of transistor is connected to P0 on Microbit.

### Software Components 

1. We can interface with outside world with P0, P1 and P2. The amount of electric current can flow thru is depended on middle leg of transistor, which is connected to P0. A variable is defined to manipulate it value, called `duty`, which will be set to 0 at beginning. `add variable`
2. add 2 `while_<condition>_do` blocks, one to speed up and the other for slow down.
3. add a `analog_write_<value>_to_pin_<P0>`
4. change `value` to `duty`

### Block Layout and Javascript

![half loop](https://www.evernote.com/l/AS41larJlGlOnLMIJwXEwHuEgAouOB4zFYUB/image.png)

Only one loop is complted.

```
let duty = 0
basic.forever(() => {
    while (duty < 1023) {
        pins.analogWritePin(AnalogPin.P0, duty)
        duty = duty + 1
    }
    while (true) {
    	
    }
})
duty = 0
```
The final construction in booklet is below.
![up and down loops](https://www.evernote.com/l/AS4zcy2bs5FG1YkC6_vaWvS1-n4nUsAW14cB/image.png)

[Share: download project](https://makecode.microbit.org/_ixMbd9CaVF85)

### Discussion

The origin construction is hard to see the changes between two loops, so I added a `pause_ms<1000>` and 2 `show_icon` to seperate them.

![](https://www.evernote.com/l/AS7YTTATBONBOKhvUHsbauqhtdBTXzOn0aIB/image.png)

```
let duty = 0
basic.forever(() => {
    basic.showIcon(IconNames.Heart)
    while (duty < 1023) {
        pins.analogWritePin(AnalogPin.P0, duty)
        duty = duty + 1
    }
    basic.pause(2000)
    basic.showIcon(IconNames.Sword)
    while (duty > 0) {
        pins.analogWritePin(AnalogPin.P0, duty)
        duty = duty - 1
    }
})
duty = 0
```
