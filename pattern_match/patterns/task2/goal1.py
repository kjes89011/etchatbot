"""Patterns for Task 1 Goal 1."""
from pattern_match import models
import re
from util import NLP, test_util


class SheIsADoctor(models.Pattern):
    def __init__(self):
        super(SheIsADoctor, self).__init__()

    def info(self, user_input):
        return None

    def match(self, user_input):
        match_result = re.match(r'^She is a doctor(.)?$', user_input.text)
        return match_result is not None


""" Testing """


def test_she_is_a_doctor_match():
    test_util.start('Testing SheIsADoctor match...')
    pattern = SheIsADoctor()
    test_util.assertion(pattern.match(NLP('She is a doctor')), True, None)
    test_util.assertion(pattern.match(NLP('She is a doctor.')), True, None)
    test_util.assertion(pattern.match(NLP('He is a doctor')), False, None)
    test_util.assertion(pattern.match(NLP('She is a Doctor')), False, None)
    test_util.result()
