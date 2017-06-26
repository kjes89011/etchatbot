"""Patterns for Task 2 Goal 3."""
from pattern_match import models
import re
from util import NLP, test_util, common


class SheIsAJob(models.Pattern):
    def __init__(self):
        super(SheIsAJob, self).__init__()
        self.regex = r'^She is a (?P<job>[a-z]*( [a-z]*)?)(.)?$'

    def info(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        return match_obj.group('job')

    def match(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        if not match_obj:
            return False
        job = match_obj.group('job')
        return job in common.JOBS


class MyMotherIsAJob(models.Pattern):
    def __init__(self):
        super(MyMotherIsAJob, self).__init__()
        self.regex = r'^My mother is a (?P<job>[a-z]*( [a-z]*)?)(.)?$'

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


def test_she_is_a_job():
    test_util.start('Testing SheIsAJob match...')
    pattern = SheIsAJob()
    test_util.assertion(pattern.match(NLP('She is a cook')), True, None)
    test_util.assertion(pattern.match(NLP('She is a taxi driver.')), True, None)
    test_util.assertion(pattern.match(NLP('He is a policeman')), False, None)
    test_util.assertion(pattern.match(NLP('She is a Cook')), False, None)
    test_util.result()


def test_my_mother_is_a_job():
    test_util.start('Testing MyMotherIsAJob match...')
    pattern = MyMotherIsAJob()
    test_util.assertion(pattern.match(
        NLP('My mother is a cook')),
        True,
        'My mother is a cook')
    test_util.assertion(pattern.match(
        NLP('My mother is a taxi driver.')),
        True,
        'My mother is a taxi driver.')
    test_util.assertion(pattern.match(
        NLP('My Mother is a policeman')),
        False,
        'My Mother is a policeman')
    test_util.assertion(pattern.match(
        NLP('My mother is a Cook')),
        False,
        'My mother is a Cook')
    test_util.result()
