#!/usr/bin/env python3
'''Etch-A-Sketch game'''
from turtle import Turtle, Screen


tim = Turtle()
tim.width(3)
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_ctrclockwise():
    tim.left(10)

def cl_scr():
    tim.clear()
    tim.penup()
    tim.home() 
    tim.pendown()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_ctrclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=cl_scr)
screen.listen()

screen.exitonclick()