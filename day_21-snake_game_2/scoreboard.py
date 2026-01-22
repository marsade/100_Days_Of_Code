#!/usr/bin/env python3
'''Scoreboard class'''
from turtle import Turtle


class Scoreboard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.write(f'Score: {self.score}', align="center", font=('Arial', 11, 'bold'))
        self.hideturtle()

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align="center", font=('Arial', 12, 'bold'))