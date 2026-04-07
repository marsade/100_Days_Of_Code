#!/usr/bin/env python3
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as f:
    names_list = f.readlines()

# header = contents[0]
# ft_header = header.strip(",\n")

with open("Input/Letters/starting_letter.txt") as f:
    contents = f.read()
    for name in names_list:
        name = name.strip("\n")
        letter = contents.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", "w") as f:
            f.write(letter)
