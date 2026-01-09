# Day 18 - Turtle & the Graphical User Interface(GUI), Importing Modules, Installing Packages and Working with Aliases

## Overview
### Basic Import
``` 
import Turtle

tim = turtle.Turtle()

```

### from...import
(keyword)		(Module Name)		(keyword)		(thing in module) <br>
from			turtle			import		Turtle

```
from turtle import Turtle

tim = Turtle()
terry = Turtle()
```

### Aliasing Modules
```
import turtle as t
tim = t.Turtle()
```

### Installing Modules
There are some modules you can't just import because they aren't packaged within the python library. Get and install external modules from [Python Package Index](https://pypi.org/project/pip/)

### Tuples
A tuple is very similar to a list, it consists of round brackets and each items in the tuple are ordered. A tuplie is immutable meaning you cant change the values like with lists.
## Challenges
- [1. Draw a square](main1.py)
- [2. Draw a dotted line](main2.py)
- [3. Drawing Different Shapes](main3.py)
- [4. Generate a random walk](main4.py)
