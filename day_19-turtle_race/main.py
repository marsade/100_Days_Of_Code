#!/usr/bin/env python3
'''Turtle Event Listeners'''
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.onkey(key="space", fun=move_forwards)
screen.listen()
screen.exitonclick()