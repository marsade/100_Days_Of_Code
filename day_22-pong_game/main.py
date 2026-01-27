#!/usr/bin/env python3
import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

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

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > \
       330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.incr_speed()

    # Detect out of bounds(r_paddle)
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect out of bounds(l_paddle)
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

scr.exitonclick()
