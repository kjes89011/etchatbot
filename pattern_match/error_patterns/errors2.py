"""Custom errors for Task 2."""
from pattern_match import models, common_regex
import re
from util import test_util, NLP, common
from pattern_match.error_patterns import common as common_errors


def errors(goal_number):
    lists = {
        1: common_errors.all_errors()
           + [WrongSubject(), CapitalizedDoctor(), WrongJob('doctor')],
        2: common_errors.all_errors()
           + [WrongSubject2(), CapitalizedCook(), WrongJob('cook')],
        3: common_errors.all_errors()
           + [CapitalizedMother()],
        4: common_errors.all_errors()
           + [CapitalizedFather()],
        5: common_errors.all_errors()
           + [TooShortAnswer(), MissingComma(), Yes()],
        6: common_errors.all_errors()
           + [WrongJob('nurse')]
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


class WrongJob(models.ErrorPattern):
    def __init__(self, expected_job):
        super(WrongJob, self).__init__()
        # She/He makes this reusable for goal 2
        self.regex = r'(She|He) is a %s(.)?$' % common_regex.JOB
        self.expected_job = expected_job

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


# Goal 4


class CapitalizedFather(models.ErrorPattern):
    def __init__(self):
        super(CapitalizedFather).__init__()

    def match(self, user_input):
        if re.match(r'^My Father is a %s(.)?$' % common_regex.JOB,
                    user_input.text):
            return models.ErrorResult(True, "Don't use a big 'F' for father.")
        else:
            return models.ErrorResult(False)


# Goal 5


class MissingComma(models.ErrorPattern):
    def __init__(self):
        super(MissingComma, self).__init__()
        self.regex = r"^No he (is not|isn't)(.)?$"

    def match(self, user_input):
        if re.match(self.regex, user_input.text):
            return models.ErrorResult(True, 'You must use a comma "," '
                                            'after "No"')
        else:
            return models.ErrorResult(False)


class Yes(models.ErrorPattern):
    def __init__(self):
        super(Yes, self).__init__()

    def match(self, user_input):
        if re.match(r'Yes(, he is)?(.)?$', user_input.text):
            return models.ErrorResult(True, 'Wrong answer.')
        return models.ErrorResult(False)


class WrongSubject5(models.ErrorPattern):
    def __init__(self):
        super(WrongSubject5, self).__init__()

    def match(self, user_input):
        if re.match(r"^((Yes|No), (she|it)|(She|It)) (is|isn't)(.)?$",
                    user_input.text):
            return models.ErrorResult(True, 'He is a man. You must '
                                            'use "he".')
        return models.ErrorResult(False)


# Goal 6


class TooShortAnswer(models.ErrorPattern):
    def __init__(self):
        super(TooShortAnswer, self).__init__()
        self.regex = r"^(A nurse|Nurse)(.)?$"

    def match(self, user_input):
        if re.match(self.regex, user_input.text):
            return models.ErrorResult(True, "That's right, but please"
                                            "give me a full sentence...")
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
    ep = WrongJob('doctor')
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
    ep = WrongJob('cook')
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


def test_capitalized_father():
    test_util.start('Testing CapitalizedFather...')
    ep = CapitalizedFather()
    test_util.assertion(
        ep.match(NLP('My father is a cook')).has_error,
        False,
        'My father is a cook')
    test_util.assertion(
        ep.match(NLP('My Father is a cook')).has_error,
        True,
        'My Father is a cook')
    test_util.result()


def test_missing_comma():
    test_util.start('Testing MissingComma...')
    ep = MissingComma()
    test_util.assertion(
        ep.match(NLP('No he is not.')).has_error, True, 'No he is not')
    test_util.assertion(
        ep.match(NLP("No he isn't.")).has_error, True, "No he isn't")
    test_util.assertion(
        ep.match(NLP('No, he is not.')).has_error, False, 'No, he is not')
    test_util.result()


def test_yes():
    test_util.start('Testing Yes...')
    ep = Yes()
    test_util.assertion(
        ep.match(NLP('Yes, he is')).has_error, True, 'Yes, he is')
    test_util.assertion(
        ep.match(NLP("Yes")).has_error, True, "Yes")
    test_util.assertion(
        ep.match(NLP('No, he is not')).has_error, False, 'No, he is not')
    test_util.result()


def test_wrong_subject_5():
    test_util.start('Testing WrongSubject5...')
    ep = WrongSubject5()
    test_util.assertion(
        ep.match(NLP('Yes, she is')).has_error, True, 'Yes, she is')
    test_util.assertion(
        ep.match(NLP("No, she isn't")).has_error, True, "Yes")
    test_util.assertion(
        ep.match(NLP('Yes, it is')).has_error, True, 'Yes, it is')
    test_util.assertion(
        ep.match(NLP("No, it isn't")).has_error, True, "No, it isn't")
    test_util.assertion(
        ep.match(NLP("She is")).has_error, True, "She is")
    test_util.assertion(
        ep.match(NLP("She isn't")).has_error, True, "She isn't")
    test_util.assertion(
        ep.match(NLP("It is")).has_error, True, "It is")
    test_util.assertion(
        ep.match(NLP("It isn't")).has_error, True, "It isn't")
    test_util.assertion(
        ep.match(NLP('No, he is not')).has_error, False, 'No, he is not')
    test_util.result()


def test_too_short_answer():
    test_util.start('Testing TooShortAnswer...')
    ep = TooShortAnswer()
    test_util.assertion(
        ep.match(NLP('Nurse.')).has_error, True, 'Nurse')
    test_util.assertion(
        ep.match(NLP("A nurse")).has_error, True, "A nurse")
    test_util.assertion(
        ep.match(NLP('He is a nurse')).has_error, False, 'He is a nurse')
    test_util.result()


def test_wrong_job_3():
    test_util.start('Testing WrongJob 3...')
    ep = WrongJob('nurse')
    test_util.assertion(ep.match(NLP('He is a driver')).has_error,
                        True,
                        'driver')
    test_util.assertion(ep.match(NLP('He is a nurse')).has_error,
                        False,
                        'cook')
    test_util.assertion(ep.match(NLP('He is a teacher')).has_error,
                        True,
                        'teacher')
    test_util.result()
