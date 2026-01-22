#!/usr/bin/env python3
'''Scoreboard class'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color("white")
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
