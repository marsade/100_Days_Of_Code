#!/usr/bin/env python3
from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
tim.speed(10)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

for i in range(60):
    tim.setheading(6 * i)
    tim.pencolor(random_color())
    tim.circle(100)

screen = Screen()
screen.exitonclick()