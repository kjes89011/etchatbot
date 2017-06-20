"""Error pattern sets for task 1."""
import re


# error functions return 'Bool, String'
# indicating whether an error exists, and a correction message.


def what_is_your_name(user_input):
    """
    Error set:
    He is Sina.  [wrong subject]
    I am tim.    [Non-capital name]
    """
    incorrect_subjects = ['You', 'He', 'She', 'This']
    if user_input[0].text in incorrect_subjects:
        pass


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
    pass
