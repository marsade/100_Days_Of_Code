#!/usr/bin/env python3
from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["royal blue", "black", "dark green", "deep pink", "dark orange", "maroon"]

for i in range(3, 11):
    tim.color(random.choice(colors))
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

screen = Screen()
screen.exitonclick()
