#!/usr/bin/env python3
'''The Secret Auction'''
from art import logo


bids = {}
continue_bids = True
print(logo)

while continue_bids:
    name = input(f"What is your name? ").lower()
    amount = int(input(f"How much are you bidding?: $"))
    print(bids)
    more_bids = input(f"Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bids == "yes":
        print('\n' * 100)
    elif more_bids == "no":
        res = max(bids, key=bids.get)
        continue_bids = False
        print(f"The winner is {res} with a bid of {bids[res]}")