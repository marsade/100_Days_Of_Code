#!/usr/bin/env python3
'''Blackjack game'''
import random
from art import logo


cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def print_final_hand(usr_list, usr_sum, comp_list, comp_sum):
    '''Print the final hands of both players
    Args:
        usr_list (list): List of user cards
        usr_sum (int): sum of usr_list numbers
        comp_list (list): List of computer cards
        comp_sum (list): sum of comp_list numbers
    Return: None
    '''

    print(f"You final hand: {usr_list}, final score: {usr_sum}")
    print(f"Computer's final hand: {comp_list}, final score: {comp_sum}")


def usr_hit(usr_list, comp_list, comp_sum):
    '''Logic for user picking a new card

    Args:
        usr_list(list): User list of cards
        comp_list(list): Computer list of cards
        comp_sum(int): Computer total
    Return:
        run(boolean)
    '''
    new_choice = random.choice(cards_list)
    usr_list.append(new_choice)
    usr_sum = sum(usr_list)
    run = True
    if usr_sum > 21:
        print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                         comp_list=comp_list, comp_sum=comp_sum)
        print("You went over, Opponent wins! 🥺")
        run = False
    elif usr_sum == 21:
        if comp_sum == 21:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("You draw. 😏")
            run = False
        else:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("You have Blackjack. You win 🤗")
            run = False
    return run


def comp_stand(comp_sum, usr_list, usr_sum, comp_list):
    '''Logic for computer stand

    Args:
        comp_sum(int): Computer total
        usr_list(list): User list of cards
        usr_sum(int): User total
        comp_list(list): Computer list of cards
    Return:
        run(boolean)
    '''
    if comp_sum == 21:
        print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                         comp_list=comp_list, comp_sum=comp_sum)
        print("Opponent had blackjack, you lose. 🙄")
        run = False
    else:
        if usr_sum > comp_sum:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("You win! 🤗")
            run = False
        elif usr_sum == comp_sum:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("You draw. 😏")
            run = False
        else:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("You lose. 🥺")
            run = False
    return run


def play_game(cards_list):
    '''Logic for playing game

    Args:
        cards_list(list): list of all cards
    Return:
        None
    '''
    start = input("Do you want to play a game of Blackjack? \
                   Type 'y' or 'n': ").lower()
    if start == 'n':
        return
    print(logo)
    usr_list = []
    comp_list = []
    for _ in range(2):
        usr_list.append(random.choice(cards_list))
        comp_list.append(random.choice(cards_list))

    run = True
    while run:
        usr_sum = sum(usr_list)
        comp_sum = sum(comp_list)
        if usr_sum == 21:
            print_final_hand(usr_list=usr_list, usr_sum=usr_sum,
                             comp_list=comp_list, comp_sum=comp_sum)
            print("That is a blackjack: You win! 😁")
            run = False
        else:
            print(f"Your cards: {usr_list}, current score: {usr_sum}")
            print(f"Computer's first card: {comp_list[0]}")
            new_card = input("Type 'y' for a new card or 'n' to pass: ")
            if new_card == "y":
                run = usr_hit(usr_list, comp_list, comp_sum)
            elif new_card == "n":
                usr_sum = sum(usr_list)
                while comp_sum <= 16:
                    comp_list.append(random.choice(cards_list))
                    comp_sum = sum(comp_list)
                if 17 <= comp_sum <= 21:
                    run = comp_stand(comp_sum, usr_list, usr_sum, comp_list)
                else:
                    print_final_hand(usr_list=usr_list, comp_list=comp_list,
                                     comp_sum=comp_sum, usr_sum=usr_sum)
                    print("Computer went over, you win! 😁")
                    run = False
    play_game(cards_list=cards_list)


play_game(cards_list=cards_list)
