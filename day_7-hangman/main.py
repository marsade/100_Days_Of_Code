#!/usr/bin/env python3
'''Hangman'''
import random
from hangman_art import stages
from hangman_words import word_list


stages.reverse()
word_list = word_list
chosen_word = random.choice(word_list)
lives = 6
print("Welcome to Hangman!")

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print('Word to guess: ' +placeholder)

saved_display = []
game_over = False
while not game_over:
    print(f"***************{lives}/6 lives left***************".upper())
    chosen_letter = input("Guess a letter: ").lower()
    
    if chosen_letter in saved_display:
        print("You have already guessed that letter. Try again.")
    display = ""
    for letter in chosen_word:
        if letter == chosen_letter:
            display += letter
            saved_display.append(letter)
        elif letter in saved_display:
            display += letter
        else:
            display += "_"
    print(display)

    if chosen_letter not in chosen_word:
        print(f"{chosen_letter} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("***************You lose***************".upper())
            print(f"The word was: {chosen_word}")
            game_over = True
    if "_" not in display:
        print("***************You win!****************".upper())
        game_over = True

    print(stages[lives])
