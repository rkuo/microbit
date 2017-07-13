# Micro:bit

![logo](https://i2.wp.com/www.tech4goodawards.com/wp-content/uploads/2016/05/BBC-Microbit.png?fit=400%2C400&ssl=1)

[toc]

![overview](https://tinyurl.com/y9ts7kdl)

## Hardware 
There are several development board in the same spec (edge connector) as BBC micro:bit.

### Board

#### BBC micro:bit
[]()

#### Micorsoft Azure IoT
[Getting Started Guide](https://microsoft.github.io/azure-iot-developer-kit/docs/getting-started/)

### Interface
![connector](https://az742082.vo.msecnd.net/pub/xdossmmf)

### Breakout Board

[Kitronik breakout board](https://www.kitronik.co.uk/checkout/cart/configure/id/159109/)  
[SparkFun micro:bit Breakout](https://www.sparkfun.com/products/13988)  

### Sensor  

#### PIR
[PIR](https://microbit-playground.co.uk/components/PIR-sensor)  

[33](https://www.evernote.com/l/AQ2rvskZNPZOe7ehSE4Idx6ammHjDr3n2qIB/image.png)  

### Output
#### [BBC micro:bit Motor Driver Boards from Kitronik](https://www.youtube.com/watch?v=fjqPx_2IxZg)  


## Programming

### Editor 
[]()


### Language

#### Javascript
There are some built-in functions allow functional programming: map, iteration. 

##### Variable

`let` and `var` are pretty similar, but unlike `var`, `let` declares a block scope local variable, optionally initializing it to a value.

`const` can be used it for variables which values remain the same.

##### Iteration

```
// Another way i using `forEach`:
arr.forEach((current, index, inputArray) => {
    /* Do something with `current` */
});
```

##### Function

```
// Using the ES6 arrow functions
let sum = (a, b) => a + b;

// Then you can call the function like:
let result = sum(40, 2);
// => 42
```

##### Class

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

##### Inheritance
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

##### Reference

[Javascript Cookbook](https://codekingdoms.com/resources/BBC-microbit-Code-Kingdoms-Cookbook.pdf)   
[Javascript Cheatsheet/Quick Review](https://www.codementor.io/johnnyb/javascript-cheatsheet-fb54lz08k)    
[Learning Functional Programming with Javascript](https://www.codementor.io/johnnyb/javascript-cheatsheet-fb54lz08k)   
[Why Learn Functional Programming in JavaScript? (Composing Software)](https://medium.com/javascript-scene/why-learn-functional-programming-in-javascript-composing-software-ea13afc7a257)  
[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  

#### MicroPython

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


