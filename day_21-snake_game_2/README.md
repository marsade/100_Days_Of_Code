# Day 21 - Snake Game (Part 2)

## Overview
This is the second part to the snake game where the following tasks were completed
- Create snake food: Make the food for the snake.
- Detect collision with food: Know when the snake has 'eaten' the food
- Create a scoreboard: Keep track of the score
- Detect collision with wall: End the game when the snake collides with a wall.
- Detect collision with tail: End the game when the snake collides with itself.

### Concepts Learned
- Class Inheritance : The process of inheriting attributes and behaviour from an existing class
- Slicing

### Class Inheritance
```
class Fish(Animal):
	def __init__(self):
		super().__init__()
```
In this example, the Fish class is inheriting from the Animal class and the super refers to the super class (Animal). So basically, initialaise anything that the super class can do in our Fish class.

### Slicing
Slicing is a powerful method for retrieving a subset of elements from lists, tuples, or strings.
**Basic Syntax**
```
sequence[start:stop:step]
```
where
- start: index at which slice begins
- stop: index at which slice stops (not inclusive)
- step: defines the increment between each index in the slice (optional)
**Example**
To get a slice of this list from index 2 to 5
```
piano_keys["a", "b", "c", "d", "e", "f", "g"]
piano_keys[2:5]
```
prints ```["c", "d", "e"]```<br/>
**Neat tricks**
1. Providing no stop value slices the list from the index given to the end
```
piano_keys["a", "b", "c", "d", "e", "f", "g"]
piano_keys[2:]
```
prints ```["c", "d", "e", "f", "g"]```<br?>

2. Using increment
```
piano_keys["a", "b", "c", "d", "e", "f", "g"]
piano_keys[2:5:2]
```
prints every other value ```["c", "e"]```

```
piano_keys["a", "b", "c", "d", "e", "f", "g"]
piano_keys[::2]
```
prints the second value of the whole list<br/>

3. Reversing list using increment
```
piano_keys["a", "b", "c", "d", "e", "f", "g"]
piano_keys[::-1]
```
Useful trick that reverses the list

SLicing also works with tuples

## In this directory
- [main.py](main.py): Main file with all modules imported and contains main functionality
- [snake.py](snake.py): Contains snake class functionality
- [food.py](food.py): Contains the snake's food functionality
- [scoreboard.py](scoreboard.py): Keeps track of the scoring and game over states