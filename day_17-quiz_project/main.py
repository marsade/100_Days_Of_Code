#!/usr/bin/env python3
'''Quiz Project'''


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User("001", "Mars")

print(user_1.username)
