#!/usr/bin/env python3
'''Number guessing game'''
import random


CHOICE = random.randint(1, 100)
print("Welcoime to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Psst! The number is {CHOICE}")
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()

# def play_difficulty(num, diff):
lives = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid")

keep_playing = True

while lives != 0 and keep_playing:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > CHOICE:
        print("Too high")
    elif guess < CHOICE:
        print("Too low")
    elif guess == CHOICE:
        print(f"You got it! The answer was {CHOICE}")
        keep_playing = False
    lives -= 1