#!/usr/bin/env python3
'''Rock, Paper, Scissors Game'''
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? \
Enter 0 for Rock, 1 for Paper, or \
2 for Scissors: "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    print(f"You chose:\n{choices[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
