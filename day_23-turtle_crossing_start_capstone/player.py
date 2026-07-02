#!/usr/bin/env python3
'''Player class'''
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, self.new_y)


    def reset_pos(self):
        self.goto(STARTING_POSITION)
