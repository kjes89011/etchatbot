"""Commonly required regular expressions."""
import re

from pattern_match import models
from util import test_util, NLP, pos, errors

NAME = r'(?P<name>(?P<first_name>[A-Z][a-z]*)(?P<last_name>\s[A-Z][a-z]*)?)'
NUMBER = r'(?P<number>([0-9]*|[a-z]*|[A-Z][a-z]*))'
ORDINAL = r'(?P<ordinal>([0-9]*[a-z]{2}|[a-z]*|[A-z][a-z]*))'
JOB = r'(?P<job>[a-z]*( [a-z]*)?)'


def match_name(user_input):
    """Determines if the user input matches a name pattern.

    Args:
      user_input: SpaCy doc of the user input.

    Returns:
      models.Match object.

    Raises:
      ArgumentError: if the user_input is not a SpaCy doc.
    """
    errors.check_input(user_input)
    match = False
    info = None
    pattern_match = re.match(NAME, user_input.text)
    if pattern_match:
        match = True
        info = pattern_match.group('name')
    return models.Match(user_input, match, info)


def match_number(user_input):
    """Determines if the user input matches a number pattern.

    Args:
      user_input: SpaCy doc of the user input.

    Returns:
      models.Match object.

    Raises:
      ArgumentError: if the user_input is not a SpaCy doc.
    """
    errors.check_input(user_input)
    excluded = ['much', 'many', 'Much', 'Many',
                'any', 'Any', 'none', 'None']
    match = False
    info = None
    pattern_match = re.match('^' + NUMBER + '$', user_input.text)
    if pattern_match:
        info = pattern_match.group('number')
        if info not in excluded and user_input[0].tag_ in pos.NUMBER:
            match = True
    return models.Match(user_input, match, info)


def match_ordinal(user_input):
    """Determines if the user input matches an ordinal pattern.

    At this point in time we only expect to see up to 12 grades.
    Other ordinals are not expected to go beyond 12. So we will
    just use a list for this one.

    Args:
      user_input: SpaCy doc of the user input.

    Returns:
      models.Match object.

    Raises:
      ArgumentError: if the user_input is not a SpaCy doc.
    """
    errors.check_input(user_input)
    ordinals = [
        '1st', 'first', 'First',
        '2nd', 'second', 'Second',
        '3rd', 'third', 'Third',
        '4th', 'fourth', 'Fourth',
        '5th', 'fifth', 'Fifth',
        '6th', 'sixth', 'Sixth',
        '7th', 'seventh', 'Seventh',
        '8th', 'eighth', 'Eighth',
        '9th', 'ninth', 'Ninth',
        '10th', 'tenth', 'Tenth',
        '11th', 'eleventh', 'Eleventh',
        '12th', 'twelfth', 'Twelfth'
    ]
    match = False
    info = None
    if user_input.text in ordinals:
        match = True
        info = user_input.text
    return models.Match(user_input, match, info)


def test_name():
    matches = [
        (NLP('Tim'), 'Tim'),
        (NLP('Tim Niven'), 'Tim Niven')]
    non_matches = [
        NLP('tim niven'),
        NLP('toast')]
    test_util.test_matches(
        matches=matches,
        non_matches=non_matches,
        match_fn=match_name)


def test_number():
    matches = [
        (NLP('eleven'), 'eleven'),
        (NLP('Nine'), 'Nine'),
        (NLP('13'), '13')]
    non_matches = [
        NLP('much'),
        NLP('Many'),
        NLP('any'),
        NLP('None')]
    test_util.test_matches(
        matches=matches,
        non_matches=non_matches,
        match_fn=match_number)


def test_ordinal():
    matches = [
        (NLP('1st'), '1st'),
        (NLP('second'), 'second'),
        (NLP('Third'), 'Third')]
    non_matches = [
        NLP('eight'),
        NLP('many')]
    test_util.test_matches(
        matches,
        non_matches,
        match_ordinal)
