"""Patterns for Task 1 Goal 5."""
from pattern_match import models
import re
from util import NLP, test_util


class NoHeIsNot(models.Pattern):
    def __init__(self):
        super(NoHeIsNot, self).__init__()
        self.regex = r"^No(, he (isn't|is not))?(.)?$"

    def info(self, user_input):
        return None

    def match(self, user_input):
        return re.match(self.regex, user_input.text) is not None


""" Testing """


def test_no_he_is_not():
    test_util.start('Testing NoHeIsNot match...')
    pattern = NoHeIsNot()
    test_util.assertion(pattern.match(NLP('No')), True, None)
    test_util.assertion(pattern.match(NLP('No, he is not.')), True, None)
    test_util.assertion(pattern.match(NLP("No, he isn't")), True, None)
    test_util.assertion(pattern.match(NLP('Yes he is.')), False, None)
    test_util.result()
