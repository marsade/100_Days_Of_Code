#!/usr/bin/env python3
'''US States List game'''
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(730, 600)
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

turtle.mainloop()