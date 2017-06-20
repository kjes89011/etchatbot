"""Patterns for Task 1, Goal 1: What's your name?"""
from util import NLP
import re
from pattern_match import models


"""
Pattern list:
1: My name's ____.
2: My name is ____.
3: It's ____.
4: It is ____.
5: I'm ____.
6: I am ____.
7: ____.
"""


def get_patterns():
    return [
        Pattern1(),

    ]


class Pattern1(models.Pattern):
    def __init__(self):
        super(Pattern1, self).__init__()

    def match(self, user_input):
        pass

    def info(self, user_input):
        pass

    def error_check(self, user_input):
        pass
