#!/usr/bin/env python3
from turtle import Turtle, Screen

tim = Turtle()
for _ in range(20):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
