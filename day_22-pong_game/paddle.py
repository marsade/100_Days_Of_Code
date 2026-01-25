#!/usr/bin/env python3
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coor: tuple):
        super().__init__()
        self.cor = coor
        self.create_paddle(self.cor)

    def create_paddle(self, tup):
        self.shape("square")
        self.shapesize(stretch_wid=100/20, stretch_len=20/20)
        self.speed("fastest")
        self.color("white")
        self.penup()
        if tup[0] < 0:
            self.left_paddle(tup)
        elif tup[0] > 0:
            self.right_paddle(tup)

    def left_paddle(self, dim):
        self.goto(dim)

    def right_paddle(self, dim):
        self.goto(dim)

    def move_up(self):
        if self.ycor() < 242:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
