#!/usr/bin/env python3
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.left(30)

    def move(self):
        self.forward(20)