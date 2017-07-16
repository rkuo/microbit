# Learning Micro:bit

![logo](https://i2.wp.com/www.tech4goodawards.com/wp-content/uploads/2016/05/BBC-Microbit.png?fit=400%2C400&ssl=1)

[toc]

![overview](https://tinyurl.com/y9ts7kdl)

## Overview

Microbit is a small microcontroller board designed for computer education developed by BBC for teaching young kids computer. Currently, it supports C, JavaScript and MircoPython. There are several editors can be used for coding. Some of them have built-in emulator, which can emulate the device behavior and allows the developer to work without physical device.

I am using Kitronik's Inventor's Kit and started my own learning and plan to publish my learning notes. It serves as supplement of the booklet came with the kit. This series is mainly use Javascript. 

More introduction from [wikipedia](https://en.wikipedia.org/wiki/Micro_Bit) and   
[Getting Started with the micro:bit from Sparkfun](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit).

## Hardware 
There are several development board in the same spec (edge connector) as BBC micro:bit. 

### Board
* BBC micro:bit
[Microbit main website](http://microbit.org/)

### Interface and Connector
![connector](https://az742082.vo.msecnd.net/pub/xdossmmf)

The breakout connector allows us to use breadboard and jump cables instead of using allegator clips. 

![Kitronik breakout connector](https://www.kitronik.co.uk/wp/wp-content/uploads/2015/08/bbc_microbit_light_level_detector_01_800.jpg)

Kitronik's breakout board allows us to add few small devices directly to the breakout board, or connect to breadboard for more complicate experiment.

## Development Environment

There are four official code editors in the [BBC micro:bit web site](https://www.microbit.co.uk/create-code), code editor can be launched from this site:

* CodeKingdoms, using JavaScript, drag and drop text based;
* Microsoft Block Editor, based on Blockly; This has been replaced with `pxt.microbit.org`
* Microsoft TouchDevelop; This is designed for mobile device.
* MicroPython, it has subset of Python.

We will use these two editor to start our experiment.

* [pxt](https://pxt.microbit.org/) (we will use this)

* [mu](https://codewith.mu/)  
This is good editor allows you to work without internet connection. But you need to download and install it on your own computer first. 

### Breakout Board
I purchased Adafurit's breakout board, but could not figure out how it works and could not find any instruction either. So, I ordered [Kitronik breakout board](https://www.kitronik.co.uk/checkout/cart/configure/id/159109/) instead.  [SparkFun micro:bit Breakout](https://www.sparkfun.com/products/13988) is also available, it needs more work to connect devices.

### Input (Sensor, Button, Video, ...)  
There are many sensors and buttons on board already. Some external sensor can be added.

* [PIR](https://microbit-playground.co.uk/components/PIR-sensor) 
* more to come ... 

### Output (Display, Relay,...)

* [BBC micro:bit Motor Driver Boards from Kitronik](https://www.youtube.com/watch?v=fjqPx_2IxZg)  

## Programming Language

### Javascript
There are some built-in functions allow functional programming: map, iteration. There are many good Javascript tutorial online, I picked up a short quick review article and partially summarized it (the part of need to know to get started) at the end of this note.  

Reference:  

[Javascript Cookbook](https://codekingdoms.com/resources/BBC-microbit-Code-Kingdoms-Cookbook.pdf)   
[Javascript Cheatsheet/Quick Review](https://www.codementor.io/johnnyb/javascript-cheatsheet-fb54lz08k)    
[Learning Functional Programming with Javascript](https://www.codementor.io/johnnyb/javascript-cheatsheet-fb54lz08k)   
[Why Learn Functional Programming in JavaScript? (Composing Software)](https://medium.com/javascript-scene/why-learn-functional-programming-in-javascript-composing-software-ea13afc7a257)  
[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  

### MicroPython
This is designed for resource constrained devices.

Reference:  

[MicroPython Differences from CPython](http://docs.micropython.org/en/latest/wipy/genrst/index.html)  
[Differences to CPython](https://github.com/micropython/micropython/wiki/Differences)  
[MicroPython](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/bbc-microbit)    
[Cheatsheet](https://microbit-playground.co.uk/cheat-sheet/)      
[MicroPython Doc](https://microbit-micropython.readthedocs.io/en/latest/)    

## Referance
[Awesome Microbit](https://github.com/carlosperate/awesome-microbit)  
[Overview](http://blog.gbaman.info/?p=711)   
[Lancaster University slides](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/Ball_Tom_FS2016_Microbit.pdf)  
[10 project](https://www.element14.com/community/community/stem-academy/microbit/blog/2016/05/26/10-bbc-microbit-projects-in-ten-days)  
[Online Cookbook](https://www.microbit.co.uk/ck)  

## Javascript Quick Overview
This summary is for someone already knows some other programming languages.

### Variable

`let` and `var` are pretty similar, but unlike `var`, `let` declares a block scope local variable, optionally initializing it to a value.

`const` can be used it for variables which values remain the same.

### Iteration

```
// Another way i using `forEach`:
arr.forEach((current, index, inputArray) => {
    /* Do something with `current` */
});
```

### Function

```
// Using the ES6 arrow functions
let sum = (a, b) => a + b;

// Then you can call the function like:
let result = sum(40, 2);
// => 42
```

### Class

```
// Using ES6 classes
class Person {
  constructor (name) {
    this.name = name;
  }
  getName () {
    return this.name;
  }
}

var p = new Person("Carol");
console.log(p.getName());
// => "Bob"
```

### Inheritance
It's also very easy to inherit classes in ES6:

```
class Musician extends Person {
   constructor (name, instrument) {
     // Call the base class
     super(name);

     this.instrument = instrument;
   }

   play () {
     console.log(`${this.getName()} is playing ${this.instrument}`);
   }
}

var me = new Musician("Johnny B.", "piano");

// Get the name of the musician, who is also a person
console.log(me.getName());
// => "Johnny B."

me.play();
// => "Johnny B. is playing piano."
```

We will skip *Callbacks*, *Promises*, *Error handling* for now.

<!--se_discussion_list:{"414OktRSuC5z1onE6S9rKsqm":{"selectionStart":0,"type":"conflict","selectionEnd":0,"discussionIndex":"414OktRSuC5z1onE6S9rKsqm"},"7w2KimTOO7GzXeVLt7QSKrur":{"selectionStart":0,"type":"conflict","selectionEnd":0,"discussionIndex":"7w2KimTOO7GzXeVLt7QSKrur"},"JHtmWPQbgua5nF410GTDqG4f":{"selectionStart":0,"type":"conflict","selectionEnd":0,"discussionIndex":"JHtmWPQbgua5nF410GTDqG4f"}}-->