"""Patterns for goal 2: Nice to meet you, too."""
from util import NLP
import re
from pattern_match import models


"""
Patterns:
1: Nice to meet you, too.
2: You, too.
"""


def get_patterns():
    return [
        Pattern1(),

    ]


class Goal2Pattern(models.Pattern):
    def __init__(self):
        super(Goal2Pattern, self).__init__()

    def info(self, user_input):
        return None


class Pattern1(Goal2Pattern):
    def __init__(self):
        super(Pattern1, self).__init__()
        self.regex = r'^Nice to meet you, too(.)?'

    def errors(self, user_input):
        # Check for ', too', and for the comma
        errors = []
        if 'too' not in user_input.text:
            errors.append('You must ')


    def match(self, user_input):
        return re.match(self.regex, user_input.text)
