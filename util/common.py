JOBS = [
    'doctor', 'nurse', 'farmer', 'bus driver',
    'shopkeeper', 'singer', 'fireman',
    'policeman', 'taxi driver', 'driver', 'teacher',
    'cook', 'postman'
]
POSITIVE_STATES = [
    'happy', 'good', 'fine', 'healthy', 'super',
    'great'
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


def head(spacy_doc):
    return next(t for t in spacy_doc if t.head == t)


def info(spacy_doc):
    for t in spacy_doc:
        print('%s\t%s\t%s' % (t.text, t.pos_, t.tag_))


def state_is_positive(state):
    """If it isn't positive, it's negative. No neutral here."""
    if state in POSITIVE_STATES or 'very ' + state in POSITIVE_STATES:
        return True
