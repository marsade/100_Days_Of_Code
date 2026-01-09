#!/usr/bin/env python3
from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)

tim = Turtle()
tim.pensize(10)
tim.speed(9)

dir = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
    
for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(dir))

screen = Screen()
screen.exitonclick()