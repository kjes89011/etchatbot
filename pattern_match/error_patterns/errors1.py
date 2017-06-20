"""Error pattern sets for task 1."""
import re
from pattern_match import models
from util import pos, NLP


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
        if len(right_children) == 1:
            target = right_children[0]
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


""" Testing """


def test_what_is_your_name():
    assert not what_is_your_name(NLP('I am Tim')).has_error
    assert what_is_your_name(NLP('I am tim')).has_error
    assert what_is_your_name(NLP('He is Tim')).has_error


def test_nice_to_meet_you():
    assert not nice_to_meet_you(NLP('Nice to meet you, too')).has_error
    assert nice_to_meet_you(NLP('Nice to meet you')).has_error
    assert nice_to_meet_you(NLP('Nice to meet you too')).has_error


def test_how_are_you():
    assert not how_are_you(NLP('I am fine, thank you')).has_error
    assert how_are_you(NLP('I am fine thank you')).has_error
    assert how_are_you(NLP('I am fine thanks')).has_error
