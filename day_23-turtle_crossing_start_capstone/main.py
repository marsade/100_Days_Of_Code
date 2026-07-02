#!/usr/bin/env python3
'''Starting point, turtle crossing game'''
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turt = Player()

cars = CarManager()
score = Scoreboard()

screen.onkey(fun=turt.move, key="Up")
loop_count = 0
game_is_on = True

while game_is_on:
    loop_count += 1
    time.sleep(0.1)

    # make a new turtle after every 6th loop
    if loop_count % 6 == 0:
        cars.create_car(1)

    # move cars across the screen
    for car in cars.cars_list:
        new_x = car.xcor() - STARTING_MOVE_DISTANCE
        car.goto(new_x, car.ycor())
        if turt.distance(car) < 30:
            score.game_over()
            game_is_on = False

    # check when player crosses finish line
    if turt.ycor() > FINISH_LINE_Y:
        new_x += MOVE_INCREMENT
        turt.reset_pos()
        score.update_score()
    screen.update()

screen.exitonclick()