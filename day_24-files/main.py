#!/usr/bin/env python3
'''File Handling'''

# Using `with` and `open` keywords to open file 
with open("~/Documents/loc.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nI haven't had breakfast")
