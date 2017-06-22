from pattern_match import models
from util import common, test_util, NLP


def all_errors():
    return [MissingVerb(), MissingDeterminer(), WrongDeterminer()]


class MissingVerb(models.ErrorPattern):
    """ Method: head is not a verb. """
    def __init__(self):
        super(MissingVerb, self).__init__()

    def match(self, user_input):
        # a one word is a one word answer, not an attempt at a sentence.
        # will be captured by the short answer rule where necessary.
        error = len(user_input) > 1 and common.head(user_input).pos_ != 'VERB'
        if error:
            return models.ErrorResult(True, 'You need to use "is"'
                                            'in your sentence.')
        return models.ErrorResult(False)


class MissingDeterminer(models.ErrorPattern):
    def __init__(self):
        super(MissingDeterminer, self).__init__()

    def match(self, user_input):
        # looking for VERB NOUN with no DET in there.
        head = common.head(user_input)
        if head.pos_ == 'VERB':
            next_token = user_input[head.i + 1]
            if next_token.pos_ == 'NOUN':
                return models.ErrorResult(True, 'You must use "a" or "an"'
                                                'before a noun like "%s"'
                                                % next_token.text)
        return models.ErrorResult(False)


class WrongDeterminer(models.ErrorPattern):
    def __init__(self):
        super(WrongDeterminer, self).__init__()

    def match(self, user_input):
        head = common.head(user_input)
        if head.pos_ == 'VERB':
            next_token = user_input[head.i + 1]
            if next_token.pos_ == 'DET':
                noun = user_input[head.i + 2]
                vowel_at_front = noun.text[0] in common.VOWELS
                if vowel_at_front and next_token.text == 'a':
                    return models.ErrorResult(
                        True,
                        'If a noun (like "%s") starts with a vowel'
                        ' (%s), you must use "an".'
                         % (noun.text, ' '.join(common.VOWELS)))
                if not vowel_at_front and next_token.text == 'an':
                    return models.ErrorResult(
                        True,
                        'If a noun (like "%s") does not start with a vowel '
                        '(%s), you must use "a".'
                        % (noun.text, ' '.join(common.VOWELS)))
        return models.ErrorResult(False)


""" Testing """


def test_missing_verb():
    test_util.start('Testing MissingVerb...')
    ep = MissingVerb()
    test_util.assertion(ep.match(NLP('He a doctor')).has_error, True, None)
    test_util.assertion(ep.match(NLP('Happy')).has_error, False, None)
    test_util.assertion(ep.match(NLP('I happy')).has_error, True, None)
    test_util.assertion(ep.match(NLP('She is a doctor')).has_error, False, None)
    test_util.assertion(ep.match(NLP('She a doctor.')).has_error, True, None)
    test_util.result()


def test_missing_determiner():
    test_util.start('Testing MissingDeterminer...')
    ep = MissingDeterminer()
    test_util.assertion(ep.match(NLP('He is doctor')).has_error, True, None)
    test_util.assertion(ep.match(NLP('He is a doctor')).has_error, False, None)
    test_util.result()


def test_wrong_determiner():
    test_util.start('Testing WrongDeterminer...')
    ep = WrongDeterminer()
    test_util.assertion(ep.match(NLP('He is an doctor')).has_error, True, None)
    test_util.assertion(ep.match(NLP('He is a apple')).has_error, True, None)
    test_util.assertion(ep.match(NLP('He is an apple')).has_error, False, None)
    test_util.assertion(ep.match(NLP('He is a doctor')).has_error, False, None)
    test_util.result()
