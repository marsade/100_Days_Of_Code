#!/usr/bin/env python3
'''Password Generator App'''
import random


letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("Welcome to the Password Generator!")
let_input = int(input("How many letters would you like in your password?\n "))
num_input = int(input("How many numbers would you like in your password?\n "))
sym_input = int(input("How many symbols would you like in your password?\n "))

passwrd = []

for _ in range(let_input):
    passwrd.append(random.choice(letters))
for _ in range(num_input):
    passwrd.append(random.choice(numbers))
for _ in range(sym_input):
    passwrd.append(random.choice(symbols))
    
print(passwrd)
random.shuffle(passwrd)
print(passwrd)
print(f"Your password is: {''.join(passwrd)}")
