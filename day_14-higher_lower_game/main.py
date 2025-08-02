#!/usr/bin/env python3
'''Higher Lower Game'''
import art
import random
import game_data 
from os import system, name

# Load data
data = game_data.data
score = 0

# Choose initial options for comparison
comp_1 = random.choice(data)
a_index = data.index(comp_1)
data.pop(a_index)
comp_2 = random.choice(data)
b_index = data.index(comp_2)

def check_ans(a, b, choice, score):
    '''Check the user answer against correct one
    Args:
        a(dict): First option
        b(dict): Second option
        choice(str): User choice
        score(int): User score
    '''

    if choice == 'a':
        if a['follower_count'] > b['follower_count']:
            score += 1
            return score, a
    elif choice == 'b':
        if b["follower_count"] > a["follower_count"]:
            score += 1
            return score, b

def play_game(comp_a, comp_b, data, score):
    '''Function to start game
    Args:
        comp_a(dict): First option
        comp_b(dict): Second option
        data(dict): dict of all options
        score(int): user score
    '''

    # Make choice strings
    str_a = f"{comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}"
    str_b = f"{comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}"

    #Print prompts
    print(art.logo)
    print(f"Compare A: {str_a}")
    print(art.vs)
    print(f"Compare B: {str_b}")
    decision = input("Who has more followers? Type 'A' or 'B': ").lower()

    try:
        score, ans = check_ans(comp_a, comp_b, decision, score)
        print(f"You're right! Current score: {score}")
        comp_a = ans
        new_comp_b = random.choice(data)
        b_pos = data.index(new_comp_b)
        data.pop(b_pos)
        if name== 'nt':
            system('cls')
        else:
            system('clear')
        play_game(comp_a, new_comp_b, data, score)
    except:
        print(f"Sorry, that's wrong. Final score {score}")
        return

play_game(comp_1, comp_2, data, score)
