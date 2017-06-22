"""Patterns for Task 1 Goal 6."""
from pattern_match import models
import re
from util import NLP, test_util


class HeIsANurse(models.Pattern):
    def __init__(self):
        super(HeIsANurse, self).__init__()
        self.regex = r"^He is a nurse(.)?$"

    def info(self, user_input):
        return None

    def match(self, user_input):
        return re.match(self.regex, user_input.text) is not None


""" Testing """


def test_he_is_a_nurse():
    test_util.start('Testing HeIsANurse match...')
    pattern = HeIsANurse()
    test_util.assertion(pattern.match(NLP('He is a nurse')), True, None)
    test_util.assertion(pattern.match(NLP('Nurse')), False, None)
    test_util.assertion(pattern.match(NLP("A nurse.")), False, None)
    test_util.result()
