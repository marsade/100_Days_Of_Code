# Importing Modules, Installing Packages and Working with Aliases

### Basic Import
``` 
import Turtle

tim = turtle.Turtle()

```

### from...import
(keyword)		(Module Name)		(keyword)		(thing in module)
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