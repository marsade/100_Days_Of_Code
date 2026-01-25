#!/usr/bin/env python3
import time
from ball import Ball
from turtle import Screen
from paddle import Paddle

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

scr.listen()
scr.onkey(fun=r_paddle.move_up, key="Up")
scr.onkey(fun=r_paddle.move_down, key="Down")

scr.onkey(fun=l_paddle.move_up, key="w")
scr.onkey(fun=l_paddle.move_down, key="s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -300:
        ball.bounce() 
scr.exitonclick()
