#!/usr/bin/env python3
# import colorgram as c
from turtle import Turtle, Screen
import turtle as t
import random

# colors = c.extract("hirst.jpg", 30)
# col_list = []
# for color in colors:
#     col_list.append(tuple(color.rgb))

# print(col_list)

rgb_values = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

tim = Turtle()
t.colormode(255)
for i in range (10):
    tim.teleport(x=0, y=i*50)
    tim.setheading(0)
    for i in range(10):
        tim.dot(20, random.choice(rgb_values))
        tim.penup()
        tim.forward(50)
screen = Screen()
screen.exitonclick()