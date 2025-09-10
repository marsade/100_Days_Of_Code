#!/usr/bin/env python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 100, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

choice = input("What would you like to order? (espresso/latte/cappuccino): ")

if choice == "espresso":
    maker = CoffeeMaker()
    print(maker.is_resource_sufficient(espresso))