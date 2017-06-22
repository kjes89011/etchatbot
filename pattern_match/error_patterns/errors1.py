"""Error pattern sets for task 1."""
import re
from pattern_match import models, common_regex
from util import NLP, test_util


# error functions return 'Bool, String'
# indicating whether an error exists, and a correction message.


def what_is_your_name(user_input):
    """
    Error set:
    1: He is Sina.  [wrong subject]
    2: I am tim.    [Non-capital name]
    """
    # 1
    incorrect_subjects = ['You', 'He', 'She', 'This']
    if user_input[0].text in incorrect_subjects:
        return models.ErrorResult(
            True, 'You must give me YOUR name. Start with "I"...')
    # 2
    head = next(t for t in user_input if t.head == t)
    if head.lemma_ == 'be':
        right_children = list(head.rights)
        if len(right_children) >= 1:
            target = right_children[0]  # first is all we want
            if target.is_lower:
                if target.pos_ == 'NOUN':
                    return models.ErrorResult(
                        True,
                        'Your name must start with a big letter: '
                        '"Steve" and not "steve".')
                if target.pos_ == 'ADJ':
                    temp = NLP(target.text)
                    if temp[0].pos_ == 'NOUN':
                        return models.ErrorResult(
                            True, 'Your name must start with a big letter: '
                                  '"Steve" and not "steve".')
    return models.ErrorResult(False)


def nice_to_meet_you(user_input):
    """
    Error set:
    Nice to meet you      [missing ', too']
    Nice to meet you too  [missing ,
    """
    r_1 = r'^Nice to meet you(.)?$'
    if re.match(r_1, user_input.text):
        return models.ErrorResult(True, 'You must say "too".')
    r_2 = r'^Nice to meet you too(.)?$'
    if re.match(r_2, user_input.text):
        return models.ErrorResult(True, 'You must use a comma before "too".')
    return models.ErrorResult(False)


def how_are_you(user_input):
    """
    Error set:
    I'm fine thank you.      [Missing comma]
    """
    if re.match(r'.*[a-z]( thank you)(.)?$', user_input.text):
        return models.ErrorResult(
            True, 'You must use a comma before "thank you".')
    if re.match(r'.*[a-z]( thanks)(.)?$', user_input.text):
        return models.ErrorResult(
            True, 'You must use a comma before "thanks".')
    return models.ErrorResult(False)


def where_are_you_from(user_input):
    """
    I am [country].
    """
    if re.match('^I am %s(.)?$' % common_regex.NAME, user_input.text):
        return models.ErrorResult(True, 'You must use "from" in this'
                                        'sentence.')
    return models.ErrorResult(False)


def how_old_are_you(user_input):
    return models.ErrorResult(False)


def what_grade_are_you_in(user_input):
    return models.ErrorResult(False)


""" Testing """


def test_what_is_your_name():
    test_util.start('Testing errors1.what_is_your_name...')
    assert not what_is_your_name(NLP('I am Tim')).has_error
    assert what_is_your_name(NLP('I am tim')).has_error
    assert what_is_your_name(NLP('He is Tim')).has_error
    test_util.result()


def test_nice_to_meet_you():
    test_util.start('Testing errors1.nice_to_meet_you...')
    assert not nice_to_meet_you(NLP('Nice to meet you, too')).has_error
    assert nice_to_meet_you(NLP('Nice to meet you')).has_error
    assert nice_to_meet_you(NLP('Nice to meet you too')).has_error
    test_util.result()


def test_how_are_you():
    test_util.start('Testing errors1.how_are_you...')
    assert not how_are_you(NLP('I am fine, thank you')).has_error
    assert how_are_you(NLP('I am fine thank you')).has_error
    assert how_are_you(NLP('I am fine thanks')).has_error
    test_util.result()


def test_where_are_you_from():
    test_util.start('Testing errors1.where_are_you_from...')
    test_util.assertion(
        where_are_you_from(NLP('I am Taiwan.')).has_error,
        True,
        'I am Taiwan')
    test_util.assertion(
        where_are_you_from(NLP('I am from Taiwan.')).has_error,
        False,
        'I am from Taiwan')
    test_util.result()


def test_how_old_are_you():
    pass


def test_what_grade_are_you_in():
    pass
