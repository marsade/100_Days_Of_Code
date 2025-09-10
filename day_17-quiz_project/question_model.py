#!/usr/bin/env python3
'''Questions for the quiz model'''


class Question():
    '''The class to create a question object'''

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
