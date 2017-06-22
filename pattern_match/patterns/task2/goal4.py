"""Patterns for Task 1 Goal 4."""
from pattern_match import models
import re
from util import NLP, test_util, common


class HeIsAJob(models.Pattern):
    def __init__(self):
        super(HeIsAJob, self).__init__()
        self.regex = r'^He is a (?P<job>[a-z]*( [a-z]*)?)(.)?$'

    def info(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        return match_obj.group('job')

    def match(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        if not match_obj:
            return False
        job = match_obj.group('job')
        return job in common.JOBS


class MyFatherIsAJob(models.Pattern):
    def __init__(self):
        super(MyFatherIsAJob, self).__init__()
        self.regex = r'^My father is a (?P<job>[a-z]*( [a-z]*)?)(.)?$'

    def info(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        return match_obj.group('job')

    def match(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        if not match_obj:
            return False
        job = match_obj.group('job')
        return job in common.JOBS


""" Testing """


def test_he_is_a_job():
    test_util.start('Testing HeIsAJob match...')
    pattern = HeIsAJob()
    test_util.assertion(pattern.match(NLP('He is a cook')), True, None)
    test_util.assertion(pattern.match(NLP('He is a taxi driver.')), True, None)
    test_util.assertion(pattern.match(NLP('She is a policeman')), False, None)
    test_util.assertion(pattern.match(NLP('He is a Cook')), False, None)
    test_util.result()


def test_my_father_is_a_job():
    test_util.start('Testing MyFatherIsAJob match...')
    pattern = MyFatherIsAJob()
    test_util.assertion(pattern.match(
        NLP('My father is a cook')),
        True,
        'My father is a cook')
    test_util.assertion(pattern.match(
        NLP('My father is a taxi driver.')),
        True,
        'My father is a taxi driver.')
    test_util.assertion(pattern.match(
        NLP('My Father is a policeman')),
        False,
        'My Father is a policeman')
    test_util.assertion(pattern.match(
        NLP('My father is a Cook')),
        False,
        'My father is a Cook')
    test_util.result()
