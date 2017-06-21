"""Custom errors for Task 2."""
from pattern_match import models, common_regex
import re
from util import test_util, NLP, common


def errors(goal_number):
    lists = {
        1: [WrongSubject(), CapitalizedDoctor(), WrongJob1()],
        2: [WrongSubject2(), CapitalizedCook(), WrongJob2()],
        3: [CapitalizedMother()],

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
            return models.ErrorResult(True, 'For a woman, use "she".')
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


class WrongJob1(models.ErrorPattern):
    def __init__(self):
        super(WrongJob1, self).__init__()
        # She/He makes this reusable for goal 2
        self.regex = r'(She|He) is a %s(.)?$' % common_regex.JOB
        self.expected_job = 'doctor'

    def match(self, user_input):
        match_obj = re.match(self.regex, user_input.text)
        if match_obj:
            job = match_obj.group('job')
            if job in common.JOBS and job != self.expected_job:
                return models.ErrorResult(True, 'Wrong answer.')
        return models.ErrorResult(False)


# Goal 2


class WrongSubject2(models.ErrorPattern):
    def __init__(self):
        super(WrongSubject2, self).__init__()

    def match(self, user_input):
        patterns = [
            r'^She is a cook(.)?$',
            r'^It is a cook(.)?$'
        ]
        result = False
        for pattern in patterns:
            if re.match(pattern, user_input.text) is not None:
                result = True
        if result:
            return models.ErrorResult(True, 'For a man, use "he".')
        else:
            return models.ErrorResult(False)


class CapitalizedCook(models.ErrorPattern):
    def __init__(self):
        super(CapitalizedCook, self).__init__()

    def match(self, user_input):
        if re.match(r'^He is a Cook(.)?$', user_input.text):
            return models.ErrorResult(True, 'For "cook" use a small "c".'
                                            'It is a noun. We only use a big'
                                            'letter for a name or at the start'
                                            'of a word.')
        else:
            return models.ErrorResult(False)


class WrongJob2(WrongJob1):
    def __init__(self):
        super(WrongJob2, self).__init__()
        self.expected_job = 'cook'


# Goal 3


class CapitalizedMother(models.ErrorPattern):
    def __init__(self):
        super(CapitalizedMother).__init__()

    def match(self, user_input):
        if re.match(r'^My Mother is a %s(.)?$' % common_regex.JOB,
                    user_input.text):
            return models.ErrorResult(True, "Don't use a big 'M' for mother.")
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


def test_wrong_job_1():
    test_util.start('Testing WrongJob1...')
    ep = WrongJob1()
    test_util.assertion(ep.match(NLP('She is a driver')).has_error,
                        True,
                        'driver')
    test_util.assertion(ep.match(NLP('She is a doctor')).has_error,
                        False,
                        'doctor')
    test_util.assertion(ep.match(NLP('She is a teacher')).has_error,
                        True,
                        'teacher')
    test_util.result()


def test_wrong_subject2():
    test_util.start('Testing WrongSubject2...')
    ep = WrongSubject2()
    test_util.assertion(ep.match(NLP('She is a cook')).has_error, True, None)
    test_util.assertion(ep.match(NLP('He is a cook')).has_error, False, None)
    test_util.assertion(ep.match(NLP('It is a cook.')).has_error, True, None)
    test_util.result()


def test_capitalized_cook():
    test_util.start('Testing CapitalizedCook...')
    ep = CapitalizedCook()
    test_util.assertion(
        ep.match(NLP('He is a cook')).has_error,
        False,
        'He is a cook')
    test_util.assertion(
        ep.match(NLP('He is a Cook')).has_error,
        True,
        'He is a Cook')
    test_util.result()


def test_wrong_job_2():
    test_util.start('Testing WrongJob2...')
    ep = WrongJob2()
    test_util.assertion(ep.match(NLP('He is a driver')).has_error,
                        True,
                        'driver')
    test_util.assertion(ep.match(NLP('He is a cook')).has_error,
                        False,
                        'cook')
    test_util.assertion(ep.match(NLP('He is a teacher')).has_error,
                        True,
                        'teacher')
    test_util.result()


def test_capitalized_mother():
    test_util.start('Testing CapitalizedMother...')
    ep = CapitalizedMother()
    test_util.assertion(
        ep.match(NLP('My mother is a cook')).has_error,
        False,
        'My mother is a cook')
    test_util.assertion(
        ep.match(NLP('My Mother is a cook')).has_error,
        True,
        'My Mother is a cook')
    test_util.result()
