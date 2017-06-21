"""Custom errors for Task 2."""
from pattern_match import models
import re
from util import test_util, NLP


def errors(goal_number):
    lists = {
        1: [WrongSubject(), CapitalizedDoctor()],

    }
    return lists[goal_number]


# Goal 1

class WrongSubject(models.ErrorPattern):
    def __init__(self):
        super(WrongSubject, self).__init__()

    def match(self, user_input):
        patterns = [
            r'^He is a doctor(.)?$',
            r'^It is a doctor(.)?$'
        ]
        result = False
        for pattern in patterns:
            if re.match(pattern, user_input.text) is not None:
                result = True
        if result:
            return models.ErrorResult(True, 'For a woman, use "She".')
        else:
            return models.ErrorResult(False)


class CapitalizedDoctor(models.ErrorPattern):
    def __init__(self):
        super(CapitalizedDoctor, self).__init__()

    def match(self, user_input):
        if re.match(r'^She is a Doctor(.)?$', user_input.text):
            return models.ErrorResult(True, 'For "doctor" use a small "d".'
                                            'It is a noun. We only use a big'
                                            'letter for a name or at the start'
                                            'of a word.')
        else:
            return models.ErrorResult(False)


""" Testing """


def test_wrong_subject():
    test_util.start('Testing WrongSubject...')
    ep = WrongSubject()
    test_util.assertion(ep.match(NLP('He is a doctor')).has_error, True, None)
    test_util.assertion(ep.match(NLP('She is a doctor')).has_error, False, None)
    test_util.assertion(ep.match(NLP('It is a doctor.')).has_error, True, None)
    test_util.result()


def test_capitalized_doctor():
    test_util.start('Testing CapitalizedDoctor...')
    ep = CapitalizedDoctor()
    test_util.assertion(
        ep.match(NLP('She is a doctor')).has_error,
        False,
        'She is a doctor')
    test_util.assertion(
        ep.match(NLP('She is a Doctor')).has_error,
        True,
        'She is a Doctor')
    test_util.result()
