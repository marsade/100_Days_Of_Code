# Day 27 - Tkinter, Creating GUIs, and Advanced Functions

## Overview
The lecture covers the fundamental components of GUIs, such as creating labels, buttons, handling button clicks, managing text inputs, and designing the layout of your application.
One of the key features discussed is advanced Python functions, including function arguments, default arguments, and the use of *args and **kwargs to accommodate variable numbers of inputs.

## What we will make
Unit Converter Program

## History of Tkinter and GUIs
- One of the earlier computers that incorporated this type of GUI OS was the Mac Lisa.

## Advanced Python Arguments
We will learn how to use advancad python arguments to specify a wider range of inputs 
- Arguments with Default Values 
These are parameters that a function can use if no specific value is provided during a function call
```py
def foo(a=3, b=4, c=6):
	print(a, b, c)

foo()

>> 3, 4, 6
```
- Unlimited Positional Arguments
This feature allows a function to accept any number of positional arguments. When you call the function with several arguments, Python collects these arguments into a tuple withing the args parameter.

```py
def add(*args):
	for n in args:
		print(n)

add(5, 6, 4, 2)
```
You can also access them by index. e.g `args[0]`
- 