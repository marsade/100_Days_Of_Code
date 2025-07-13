#!/usr/bin/env python3
'''Python Treasure Island Game'''


print("Welcome to Treasure Island!")
print('''
     ,*-~"`^"*u_                                _u*"^`"~-*,
  p!^       /  jPw                            w9j \        ^!p
w^.._      /      "\_                      _/"     \        _.^w
     *_   /          \_      _    _      _/         \     _*
       q /           / \q   ( `--` )   p/ \          \   p
       jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                *_ /      "==) ;; (=="      \ _*
                 `/.w***,   /(    )\   ,***w.\"
                  ^ ilmk ^c/ )    ( \c^      ^
                          'V')_)(_('V'
                              `` ``
''')
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go \
                left or right? (left/right) ")
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim \
                across or wait for a boat? (swim/wait) ")
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house \
                with three doors. Which door do you choose? (red/blue/yellow) ")
        if choice3 == "yellow":
            print("Congratulations! You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        elif choice3 == "red":
            print("You were burned by fire. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by a trout. Game over.")
elif choice1 == "right":
    print("You fell into a hole. Game over.")
else:
    print("You chose a direction that doesn't exist. Game over.")
