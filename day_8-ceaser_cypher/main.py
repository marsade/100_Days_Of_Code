#!/usr/bin/env python3
'''Ceaser Cypher'''
from art import logo

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def ceaser(usr_text, usr_direction, usr_shift):
    output_text = ""
    if usr_direction == "decode":
        usr_shift *= -1
    for letter in usr_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter)
            new_position = (shifted_position + usr_shift) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"Here is the encoded text: {output_text}")



run = True
while run:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(usr_text=text, usr_direction=direction, usr_shift=shift)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == "no":
        run = False
        print("Goodbye!")
