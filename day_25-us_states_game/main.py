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

df = pandas.read_csv("./50_states.csv")
right_guesses = []
score = 0

all_states = df.state.to_list()

while len(right_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?")
    usr_ans = answer_state.title()

    if usr_ans == "Exit":
        for state in right_guesses:
            if state in all_states:
                all_states.remove(state)

        states_to_learn = pandas.Series(all_states)
        states_to_learn.to_csv("states_to_learn.csv", index=False)
        break

    if usr_ans in all_states and usr_ans not in right_guesses:
        score += 1
        turt = turtle.Turtle()
        turt.penup()
        turt.hideturtle()
        x_coor = df[df.state == usr_ans].x.values[0]
        y_coor = df[df.state == usr_ans].y.values[0]
        turt.goto(x_coor, y_coor)
        turt.pendown()
        turt.write(usr_ans, font=("Arial", 10, "normal"))
        right_guesses.append(usr_ans)


turtle.mainloop()
