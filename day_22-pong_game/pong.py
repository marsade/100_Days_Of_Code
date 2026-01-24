#!/usr/bin/env python3
from turtle import Screen, Turtle


scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")

user = Turtle()
user.speed("fastest")
user.hideturtle()
user.color("white")
user.penup()
user.goto(350, 0)
user.pendown()
user.setheading(0)
user.begin_fill()
for dim in [20, 100, 20, 100]:
    user.forward(dim)
    user.right(90)
user.end_fill()

scr.exitonclick()