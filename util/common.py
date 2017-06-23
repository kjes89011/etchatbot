from util import test_util


JOBS = [
    'doctor', 'nurse', 'farmer', 'bus driver',
    'shopkeeper', 'singer', 'fireman',
    'policeman', 'taxi driver', 'driver', 'teacher',
    'cook', 'postman'
]
POSITIVE_STATES = [
    'happy', 'good', 'fine', 'healthy', 'super',
    'great', 'OK'
]
GENERIC_QUESTION_BACKS = [
    'Any you?', 'And yours?'
]
VOWELS = [
    'a', 'e', 'i', 'o', 'u'
]
NEGATIONS = [
    'not', "n't"
]
AGE_BRACKETS = {
    0: lambda age: age < 6,
    1: lambda age: 6 <= age <= 30,
    2: lambda age: 31 <= age <= 50,
    3: lambda age: 51 <= age <= 99
}
TEXT_TO_DIGIT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}
TEXT_TO_TEEN = {
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19
}
TEXT_TO_TENS = {
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}
DIGITS = list(TEXT_TO_DIGIT.keys())
TEENS = list(TEXT_TO_TEEN.keys())
TENS = list(TEXT_TO_TENS.keys())
LONE_NUMBERS = DIGITS + TEENS + TENS


def age_bracket(age):
    """Age is a string, returns an int, 1-4."""
    if age.isdigit():
        age = int(age)
    else:
        age = text_to_number(age)
    for bracket, function in AGE_BRACKETS.items():
        if function(age):
            return bracket


def head(spacy_doc):
    return next(t for t in spacy_doc if t.head == t)


def info(spacy_doc):
    for t in spacy_doc:
        print('%s\t%s\t%s' % (t.text, t.pos_, t.tag_))


def state_is_positive(state):
    """If it isn't positive, it's negative. No neutral here."""
    return state in POSITIVE_STATES \
           or state.replace('very ', '') in POSITIVE_STATES


def text_to_number(text):
    if not well_formed_number(text):
        raise Exception('Not a well-formed number: %s' % text)
    if '-' not in text:
        if text in TEXT_TO_DIGIT.keys():
            return TEXT_TO_DIGIT[text]
        elif text in TEXT_TO_TEEN.keys():
            return TEXT_TO_TEEN[text]
        elif text in TEXT_TO_TENS.keys():
            return TEXT_TO_TENS[text]
        else:
            raise Exception('How did we get to here?')
    else:
        split = text.split('-')
        if len(split) != 2:
            raise Exception('How did we get to here?')
        if split[0] not in TEXT_TO_TENS.keys():
            raise Exception('How did we get to here?')
        ten = TEXT_TO_TENS[split[0]]
        if split[1] not in TEXT_TO_DIGIT.keys():
            raise Exception('How did we get to here?')
        digit = TEXT_TO_DIGIT[split[1]]
        return ten + digit


def well_formed_number(text):
    """Can be either:
    - digit or teen
    - ten-digit
    """
    text = text.lower()
    if '-' not in text:
        return text in LONE_NUMBERS
    else:
        split = text.split('-')
        if len(split) != 2:
            return False
        ten = split[0]
        digit = split[1]
        return ten in TENS and digit in DIGITS


""" Testing """


def test_age_bracket():
    test_util.start('Testing age_bracket...')
    test_util.assertion(
        age_bracket('5'),
        0,
        '5')
    test_util.assertion(
        age_bracket('five'),
        0,
        'five')
    test_util.assertion(
        age_bracket('7'),
        1,
        '7')
    test_util.assertion(
        age_bracket('seven'),
        1,
        'seven')
    test_util.assertion(
        age_bracket('31'),
        2,
        '31')
    test_util.assertion(
        age_bracket('thirty-one'),
        2,
        'thirty-one')
    test_util.assertion(
        age_bracket('51'),
        3,
        '51')
    test_util.assertion(
        age_bracket('fifty-one'),
        3,
        'fifty-one')
    test_util.result()


def test_state_is_positive():
    test_util.start('Testing state_is_positive...')
    test_util.assertion(
        state_is_positive('happy'),
        True,
        'happy')
    test_util.assertion(
        state_is_positive('very happy'),
        True,
        'very happy')
    test_util.assertion(
        state_is_positive('sad'),
        False,
        'sad')
    test_util.assertion(
        state_is_positive('OK'),
        True,
        'OK')
    test_util.result()


def test_text_to_number():
    test_util.start('Testing text_to_number...')
    test_util.assertion(
        text_to_number('one'),
        1,
        'one')
    test_util.assertion(
        text_to_number('two'),
        2,
        'two')
    test_util.assertion(
        text_to_number('three'),
        3,
        'three')
    test_util.assertion(
        text_to_number('four'),
        4,
        'four')
    test_util.assertion(
        text_to_number('five'),
        5,
        'five')
    test_util.assertion(
        text_to_number('six'),
        6,
        'six')
    test_util.assertion(
        text_to_number('seven'),
        7,
        'seven')
    test_util.assertion(
        text_to_number('eight'),
        8,
        'eight')
    test_util.assertion(
        text_to_number('nine'),
        9,
        'nine')
    test_util.assertion(
        text_to_number('ten'),
        10,
        'ten')
    test_util.assertion(
        text_to_number('eleven'),
        11,
        'eleven')
    test_util.assertion(
        text_to_number('twelve'),
        12,
        'twelve')
    test_util.assertion(
        text_to_number('thirteen'),
        13,
        'thirteen')
    test_util.assertion(
        text_to_number('fourteen'),
        14,
        'fourteen')
    test_util.assertion(
        text_to_number('fifteen'),
        15,
        'fifteen')
    test_util.assertion(
        text_to_number('sixteen'),
        16,
        'sixteen')
    test_util.assertion(
        text_to_number('seventeen'),
        17,
        'seventeen')
    test_util.assertion(
        text_to_number('eighteen'),
        18,
        'eighteen')
    test_util.assertion(
        text_to_number('nineteen'),
        19,
        'nineteen')
    test_util.assertion(
        text_to_number('twenty'),
        20,
        'twenty')
    test_util.assertion(
        text_to_number('twenty-one'),
        21,
        'twenty-one')
    test_util.result()


def test_well_formed_number():
    test_util.start('Testing well_formed_number...')
    test_util.assertion(
        well_formed_number('one'),
        True,
        'one')
    test_util.assertion(
        well_formed_number('two'),
        True,
        'two')
    test_util.assertion(
        well_formed_number('three'),
        True,
        'three')
    test_util.assertion(
        well_formed_number('four'),
        True,
        'four')
    test_util.assertion(
        well_formed_number('five'),
        True,
        'five')
    test_util.assertion(
        well_formed_number('six'),
        True,
        'six')
    test_util.assertion(
        well_formed_number('seven'),
        True,
        'seven')
    test_util.assertion(
        well_formed_number('eight'),
        True,
        'eight')
    test_util.assertion(
        well_formed_number('nine'),
        True,
        'nine')
    test_util.assertion(
        well_formed_number('ten'),
        True,
        'ten')
    test_util.assertion(
        well_formed_number('eleven'),
        True,
        'eleven')
    test_util.assertion(
        well_formed_number('twelve'),
        True,
        'twelve')
    test_util.assertion(
        well_formed_number('thirteen'),
        True,
        'thirteen')
    test_util.assertion(
        well_formed_number('fourteen'),
        True,
        'fourteen')
    test_util.assertion(
        well_formed_number('fifteen'),
        True,
        'fifteen')
    test_util.assertion(
        well_formed_number('sixteen'),
        True,
        'sixteen')
    test_util.assertion(
        well_formed_number('seventeen'),
        True,
        'seventeen')
    test_util.assertion(
        well_formed_number('eighteen'),
        True,
        'eighteen')
    test_util.assertion(
        well_formed_number('nineteen'),
        True,
        'nineteen')
    test_util.assertion(
        well_formed_number('twenty'),
        True,
        'twenty')
    test_util.assertion(
        well_formed_number('twenty-one'),
        True,
        'twenty-one')
    test_util.assertion(
        well_formed_number('twenty one'),
        False,
        'twenty one')
    test_util.assertion(
        well_formed_number('one-twenty'),
        False,
        'one-twenty')
    test_util.result()
