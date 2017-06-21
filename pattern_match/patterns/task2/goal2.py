"""Patterns for Task 1 Goal 2."""
from pattern_match import models
import re
from util import NLP, test_util


class HeIsACook(models.Pattern):
    def __init__(self):
        super(HeIsACook, self).__init__()

    def info(self, user_input):
        return None

    def match(self, user_input):
        match_result = re.match(r'^He is a cook(.)?$', user_input.text)
        return match_result is not None


""" Testing """


def test_he_is_a_cook():
    test_util.start('Testing SheIsADoctor match...')
    pattern = HeIsACook()
    test_util.assertion(pattern.match(NLP('He is a cook')), True, None)
    test_util.assertion(pattern.match(NLP('He is a cook.')), True, None)
    test_util.assertion(pattern.match(NLP('She is a cook')), False, None)
    test_util.assertion(pattern.match(NLP('He is a Cook')), False, None)
    test_util.result()
