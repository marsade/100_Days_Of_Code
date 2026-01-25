#!/usr/bin/env python3
import time
from turtle import Screen, Turtle


scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

user = Turtle("square")
user.shapesize(stretch_wid=100/20, stretch_len=20/20)
user.speed("fastest")
user.color("white")
user.penup()
user.goto(350, 0)


def move_up():
    if user.ycor() < 242:
        user.sety(user.ycor() + 20)


def move_down():
    if user.ycor() > -240:
        user.sety(user.ycor() - 20)


scr.listen()
scr.onkey(fun=move_up, key="Up")
scr.onkey(fun=move_down, key="Down")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.2)

scr.exitonclick()
