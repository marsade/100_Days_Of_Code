# Day 27 - Tkinter, Creating GUIs, and Advanced Functions

## Overview
The lecture covers the fundamental components of GUIs, such as creating labels, buttons, handling button clicks, managing text inputs, and designing the layout of your application.
One of the key features discussed is advanced Python functions, including function arguments, default arguments, and the use of *args and **kwargs to accommodate variable numbers of inputs.

## What we will make
Unit Converter Program

## History of Tkinter and GUIs
- One of the earlier computers that incorporated this type of GUI OS was the Mac Lisa.

## Advanced Python Arguments
We will learn how to use advanced python arguments to specify a wider range of inputs 
- Arguments with Default Values :
These are parameters that a function can use if no specific value is provided during a function call
```py
def foo(a=3, b=4, c=6):
	print(a, b, c)

foo()

>> 3, 4, 6
```
- Unlimited Positional Arguments:
This feature allows a function to accept any number of positional arguments. When you call the function with several arguments, Python collects these arguments into a tuple withing the args parameter.

```py
def add(*args):
	for n in args:
		print(n)

add(5, 6, 4, 2)
```
You can also access them by index. e.g `args[0]`
- Many Keyworded Arguments:
The double asterisks allows us to work with an arbitrary number of keyword arguments.
```py
def
```
## .get() function
We can use `.get()` instead of square brackets to access key-values in dictionaries. The benefit of get is that it won't return an error if the key is not found, just None.
```py
se;f.make = kw.get("make")
```
## Tkinter Layout Managers
Tkinter has a whole bunch of different layour managers. There are three you should know about.
- Pack: It packs each widget next to each other in a vaguely logical format. By default, pack will always start from the top and pack every other widget just below the previous one. The problem with pack is that it is quite difficult to specify a precise position.
- Place: When you place something, you can provide a x and y value. If a widget gets created and is doesnt have any layout specified then it wont be shown
```py
my_label.place(x=100, y=100)
```
The problem with place is that it is simple enough for a minimum number of widgets but as that starts to grow it becomes difficult to manage the precise position of each one.
- Grid: It imagines that the entire program is a grid and you can divide it into any number of columns and rows as you want to.
```py
my_label.grid(column=0, row=0)
```
The position of the widets is relative to other widgets placed on the screen.