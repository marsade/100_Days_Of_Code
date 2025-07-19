#!/usr/bin/env python3
"""Calculator app"""
from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operations["*"](4, 8))
new_num1 = None
while True:
    if new_num1 is not None:
        num1 = new_num1
    else:
        print(logo)
        num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    res = operations[op](num1, num2)
    print(f"{num1} {op} {num2} = {res}")
    restart = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
    if restart == 'y':
        new_num1 = res
    else:
        new_num1 = None
        print("\n" * 20)
