#!/usr/bin/env python3
import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        # super().__init__()
        self.cars_list = []
        self.create_car(15)

    def create_car(self, num):
        for i in range(num):
            t = Turtle("square")
            t.shapesize(stretch_len=2)
            t.penup()
            t.color(random.choice(COLORS))
            self.new_y = random.randrange(-220, 240, 3)
            self.new_x = random.randrange(290, 1500, 2)
            t.goto(self.new_x, self.new_y)
            self.cars_list.append(t)

    # def incr(self):
    #     for car in self
