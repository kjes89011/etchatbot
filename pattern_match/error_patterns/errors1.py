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
    pass


def how_are_you(user_input):
    """
    Error set:
    I am nice    [incorrect adjective]
    """
    incorrect_adjectives = ['nice', '']


""" Testing """


def test_what_is_your_name():
    r1 = what_is_your_name(NLP('I am Tim'))
    assert not r1.has_error
    r2 = what_is_your_name(NLP('I am tim'))
    assert r2.has_error
    r3 = what_is_your_name(NLP('He is Tim'))
    assert r3.has_error
