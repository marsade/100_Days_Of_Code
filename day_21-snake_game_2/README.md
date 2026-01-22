# Day 21 - Snake Game (Part 2)

## Overview
### Concepts Learned
- Class Inheritance : The process of inheriting attributes and behaviour from an existing class
- Slicing

#### Class Inheritance
```
class Fish(Animal):
	def __init__(self):
		super().__init__()
```
In this example, the Fish class is inheriting from the Animal class and the super refers to the super class (Animal). So basically, initialaise anything that the super class can do in our Fish class.

## In this directory
- [main.py](main.py): Main file with all modules imported and contains main functionality
- [snake.py](snake.py): Contains snake class functionality
- [food.py](food.py): Contains the snake's food functionality