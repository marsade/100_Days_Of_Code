# Day 19 - More Turtle Graphics, Evemt Listeners, State and Multiple Instances

## Overview
### Functions as an input
We have function_a...
```
def function_a(something):
	# Do this
	# Then do this
```
Then we have function_b...
```
def function_b():
	# Do this
```
We can pass function_be into function_a like so...
```
	function_a(function_b)
```
When we pass the function as an input, we only pass the name and not the parantheses. In python, this is called **higher order functions**

### Object State and Instances
A class functions as a blueprint to define the properties and behaviours of its objects (turtles in this case). From this class, you can create individual turtle objects, each referred to as an **instance** of the turtle class. Multiple instances of a single class can exist, each with its unique state. In programming, the **state** of an object is when it can have different attributes and can be performing different methods. E.g the state of one turtle object's color attribute could be green and another could be red.

## Challenges - Etch-A-Sketch, Turle Race
- [1. intro to event listeners and higher order functions](main.py)
- [2. Etch-A-Sketch](main2.py)
- [3. Turtle Race](main3.py)