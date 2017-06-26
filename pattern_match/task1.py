"""Matching input patterns for Task 1."""
import re
from pattern_match import common_regex, models
from util import pos, test_util, NLP, errors, common
from pattern_match.patterns.task1 import goal1, goal2
from pattern_match.error_patterns import errors1


def no_match(user_input):
    return models.Match(user_input, False, None)


class TempWrapper:
    """Temporary wrapper object to hook this up to the interface."""
    def __init__(self, match_function, error_function):
        self.match_function = match_function
        self.error_function = error_function

    def error(self, user_input):
        return self.error_function(user_input)

    def info(self, user_input):
        return self.match_function(user_input).info

    def match(self, user_input):
        return self.match_function(user_input).match


# This deprecated for now... might pick it back up in task2.
def get_goals():
    return [
        models.Goal(goal1.get_patterns(), True),
        models.Goal(goal2.get_patterns(), False),

    ]


# this is how we are handling task1.
def goal(number):
    """Interface for getting to Pattern check objects for goals.

    Usage from calling code:
    from pattern_match import matching  # imports all task files
    result = matching.task(1).goal(1).--function--(user_input),
    where --function-- is in the set {match, info, errors}.
    The output of this will vary depending on the function.

    Args:
      number: the goal number.

    Returns:
      function accepting a SpaCy document of user input,
        which returns an object (depending on the function)
        bool indicating whether the input is a match to
        the requirements, and optionally any info that
        needs to be extracted from the input.

    Raises:
      InvalidKeyError: if the goal number is not in the set of
        expected values.
    """
    goals = {
        1: TempWrapper(match_name,
                       errors1.what_is_your_name),
        2: TempWrapper(match_nice_to_meet_you,
                       errors1.nice_to_meet_you),
        3: TempWrapper(match_how_are_you_response,
                       errors1.how_are_you),
        4: TempWrapper(match_where_are_you_from_response,
                       errors1.where_are_you_from),
        5: TempWrapper(match_how_old_are_you_response,
                       errors1.how_old_are_you),
        6: TempWrapper(match_what_grade_are_you_in_response,
                       errors1.what_grade_are_you_in)}
    if number not in goals.keys():
        raise errors.InvalidKeyError(number, goals.keys())
    return goals[number]


def match_name(user_input):
    """Match user input pattern for task 1.1.

    I look for PRP VBP NNP.

    pattern = db.get(...)


    PATTERN MATCHED:
    BOT: What's your name?
    USR:
    [option_set]
    1: My name's ____.
    2: My name is ____.
    3: It's ____.
    4: It is ____.
    5: I'm ____.
    6: I am ____.
    7: ____.
    [/option_set]

    INFO RETURNED:
    The user's name.

    ISSUES:
    - Deal with punctuation - i.e. full stop?
    - What if they forget to capitalize their name?

    Args:
      user_input: the user input (SpaCy doc)

    Returns:
      models.Match object.
    """
    regexs = [
        r"^My name's %s(.)?$" % common_regex.NAME,
        r'^My name is %s(.)?$' % common_regex.NAME,
        r"^It's %s(.)?$" % common_regex.NAME,
        r'^It is %s(.)?$' % common_regex.NAME,
        r"^I'm %s(.)?$" % common_regex.NAME,
        r'^I am %s(.)?$' % common_regex.NAME,
        r'^%s(.)?$' % common_regex.NAME
    ]
    match = False
    info = None
    for r in regexs:
        pattern_match = re.match(r, user_input.text)
        if pattern_match:
            info = pattern_match.group('name')
            if info not in common.INVALID_NAMES:
                match = True
    return models.Match(user_input, match, info)


def match_nice_to_meet_you(user_input):
    """Match user input pattern for task 1.2.

    PATTERN MATCHED:
    BOT: Nice to meet you.
    USR: Nice to meet you, too.

    You, too.
    Happy|Glad to meet you, too.

    INFO RETURNED:
    None.

    Args:
      user_input: the user input (SpaCy doc).

    Returns:
      models.Match object.
    """
    r = r'^Nice to meet you, too(.)?'
    match = False
    info = None
    if re.match(r, user_input.text):
        match = True
    return models.Match(user_input, match, info)


def match_how_are_you_response(user_input):
    """Match user input pattern for task 1.3.

    PATTERN MATCHED:
    BOT: How are you today?
    USR: [options]
    I am {state}(, thank you|thanks)
    I'm {state}(, thank you|thanks)
    {State}(, thank you|thanks)
    I have a cold
    Not bad
    Not too bad
    I feel happy
    [/options]

    INFO RETURNED:
    The user's state.

    ISSUES:
    - There is a lot of potential variation in the state.
      Therefore make this a regex group, extract it, and process
      it separately.

    Args:
      user_input: the user input (SpaCy doc).

    Returns:
      models.Match object.
    """
    match = False
    info = None
    r1 = r"^(I'm |I am )?" \
        r"(very |not )?" \
        r"(?P<state>([A-Z]{1}[a-z]*)|[a-z-]*)" \
        r"(, thank you|, thanks)?(.)?$"
    r2 = r'^I have (?P<state>(a cold|the flu))(.)?$'
    cold_flu = ['a cold', 'the flu']
    pattern_match1 = re.match(r1, user_input.text)
    pattern_match2 = re.match(r2, user_input.text)
    if pattern_match1:
        modifier = pattern_match1.group(2)
        state = pattern_match1.group(3)
        # state should be an adjective
        info_tok = NLP(state)[0]
        if info_tok.tag_ in pos.ADJECTIVES:
            match = True
            info = state
            if modifier:
                info = modifier + state
    elif pattern_match2:
        state = pattern_match2.group(1)
        if state in cold_flu:
            match = True
            info = state
    # if we don't have a match thus far...
    if not match:
        # try some more complicated methods
        head = common.head(user_input)
        acceptable_head_lemmas = ['be', 'have']
        # check the subject is 'I'
        if 'I' in [t.text for t in head.lefts]:
            # check the object for a match
            pass
    return models.Match(user_input, match, info)


def match_where_are_you_from_response(user_input):
    """Match user input pattern for task 1.4.

    PATTERN MATCHED:
    BOT: Where are you from?
    USR: [options]
    I am from {Place}
    I'm from {Place}
    {Place}
    [/options]

    INFO RETURNED:
    Where the user is from.

    ISSUES:
    - What if the respond with an ethnicity: e.g. I'm Taiwanese?
    - To really validate this input we need to make sure they
      say a place, e.g. "Taiwan", and not something silly like
      "Earth".

    Args:
      user_input: the user input (SpaCy doc).

    Returns:
      models.Match object.
    """
    r = r"^(I'm from |I am from )?%s(.)?$" % common_regex.NAME  # same as place
    match = False
    info = None
    pattern_match = re.match(r, user_input.text)
    if pattern_match:
        match = True
        info = pattern_match.group('name')
    return models.Match(user_input, match, info)


def match_how_old_are_you_response(user_input):
    """Match user input pattern for task 1.5.

    PATTERN MATCHES:
    BOT: How old are you?
    USR: [options]
    I am {age} years old
    I'm {age} years old
    I am {age}
    I'm {age}
    {age} years old
    {age}
    [/options]

    INFO RETURNED:
    The user's age.

    ISSUES:
    - The age could be given as text or a number.

    Args:
      user_input: the user input (SpaCy doc).

    Returns:
      models.Match object.
    """
    r = r'^' \
        r"(I am |I'm )?" \
        r"%s" % common_regex.NUMBER + \
        r"( years old)?" \
        r'(.)?' \
        r'$'
    match = False
    info = None
    pattern_match = re.match(r, user_input.text)
    if pattern_match:
        info = pattern_match.group('number')
        age_match = common_regex.match_number(NLP(info))
        match = age_match.match
    return models.Match(user_input, match, info)


def match_what_grade_are_you_in_response(user_input):
    """Match user input pattern for task 1.6.

    PATTERN MATCHES:
    BOT: What grade are you in?
    USR: [options]
    I am in the {ordinal} grade.
    I'm in the {ordinal} grade.
    The {ordinal} grade.
    [/options]

    INFO RETURNED:
    The user's grade.

    ISSUES:
    -

    Args:
      user_input: the user input (SpaCy doc).

    Returns:
      models.Match object.
    """
    r = r'^' \
        r"(I am in |I'm in )?" \
        r'(The |the )' \
        r"%s" % common_regex.ORDINAL + \
        r"( grade)" \
        r'(.)?' \
        r'$'
    match = False
    info = None
    pattern_match = re.match(r, user_input.text)
    if pattern_match:
        info = pattern_match.group('ordinal')
        ordinal_match = common_regex.match_ordinal(NLP(info))
        match = ordinal_match.match
    return models.Match(user_input, match, info)


#
# Testing


def test_match_name():
    matches = [
        (NLP("My name's Tim."), 'Tim'),
        (NLP('My name is Bob'), 'Bob'),
        (NLP("It's Henry."), 'Henry'),
        (NLP('It is Frank'), 'Frank'),
        (NLP("I'm Hank"), 'Hank'),
        (NLP('I am Joe.'), 'Joe'),
        (NLP('Satan.'), 'Satan')]
    non_matches = [
        NLP('What is your name?'),   # far out
        NLP('My name is tim.'),      # missing capital
        NLP('Hi'),
        NLP('hi'),
        NLP('My nome it Tim')]      # spelling mistakes
    test_util.test_matches(matches, non_matches, match_name)


def test_match_nice_to_meet_you():
    matches = [
        (NLP('Nice to meet you, too'), None),
        (NLP('Nice to meet you, too.'), None)]
    non_matches = [
        NLP('Nice to meet you too')]  # missing comma
    test_util.test_matches(matches, non_matches, match_nice_to_meet_you)


def test_match_how_are_you_response():
    matches = [
        (NLP('I am happy, thank you'), 'happy'),
        (NLP("I'm good, thanks"), 'good'),
        (NLP('I am fine.'), 'fine'),
        (NLP("I'm sad"), 'sad'),
        (NLP('Healthy, thank you.'), 'Healthy'),
        (NLP('I am not good'), 'not good'),
        (NLP('I am very happy'), 'very happy'),
        (NLP('I have a cold'), 'a cold'),
        (NLP('I have a cold.'), 'a cold'),
        (NLP('I have the flu'), 'the flu'),
        (NLP('I am happy, thanks.'), 'happy')]
    non_matches = [
        NLP('I am banana, thank you.'),
        NLP('I am fine thank you.'),
        NLP('I am a small village near the sea, thank you.'),
        NLP('I have a toy')]
    test_util.test_matches(matches, non_matches, match_how_are_you_response)


def test_match_where_are_your_from_response():
    matches = [
        (NLP('I am from New Zealand'), 'New Zealand'),
        (NLP("I'm from Taiwan."), 'Taiwan'),
        (NLP('Iran.'), 'Iran')]
    non_matches = [
        NLP('I am an elephant'),
        NLP('I am Taiwan.'),
        NLP('I am from taiwan')]
    test_util.test_matches(matches,
                           non_matches,
                           match_where_are_you_from_response)


def test_match_how_old_are_you_response():
    matches = [
        (NLP('I am eight years old'), 'eight'),
        (NLP("I'm 9 years old"), '9'),
        (NLP('I am thirteen'), 'thirteen'),
        (NLP("I'm twenty"), 'twenty'),
        (NLP('Seven years old'), 'Seven'),
        (NLP('11'), '11')]
    non_matches = []
    test_util.test_matches(matches,
                           non_matches,
                           match_how_old_are_you_response)


def test_match_what_grade_are_you_in_response():
    matches = [
        (NLP('I am in the 7th grade.'), '7th'),
        (NLP("I'm in the eighth grade."), 'eighth'),
        (NLP('The Ninth grade.'), 'Ninth'),
    ]
    non_matches = [
        NLP('I am in the eight grade.')
    ]
    test_util.test_matches(matches,
                           non_matches,
                           match_what_grade_are_you_in_response)
