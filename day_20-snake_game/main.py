#!/usr/bin/env python3
from turtle import Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()

scr.listen()
scr.onkey(key="Up", fun=snake.up)
scr.onkey(key="Down", fun=snake.down)
scr.onkey(key="Left", fun=snake.left)
scr.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    scr.update() 
    time.sleep(0.2)

    snake.move()
scr.exitonclick()