"""Custom errors for this module."""
import spacy


class Error(Exception):
    """Base error class for custom errors."""
    pass


class IntegrityError(Error):
    """An integrity check failed.

    Attributes:
      message: A descriptive message of the integrity error.
    """

    def __init__(self, message):
        self.message = message


class InvalidKeyError(Error):
    """An invalid key was passed.

    Attributes:
      key_passed: the key passed.
      valid_options: the set of valid options.
    """

    def __init__(self, key_passed, valid_options):
        self.key_passed = key_passed
        self.valid_options = valid_options


class TypeError(Error):
    """An invalid argument was passed.

    Attributes:
      argument_type: the type of the argument passed.
      expected_argument_type: the type expected.
    """

    def __init__(self, argument_type, expected_argument_type):
        self.argument_type = argument_type
        self.expected_argument_type = expected_argument_type


class ValueError(Error):
    """An argument has an invalid value.

    Attributes:
      received_value: the value received,
      acceptable_values: String describing acceptable values.
    """

    def __init__(self, received_value, acceptable_values):
        self.received_value = received_value
        self.acceptable_values = acceptable_values


def check_input(user_input):
    """Reusable method to check user input is a Spacy doc.

    Args:
      user_input: the user input to check.

    Raises:
      TypeError if user input is not a Spacy doc.
    """
    if not isinstance(user_input, spacy.tokens.doc.Doc):
        raise TypeError(
            argument_type=type(user_input),
            expected_argument_type=spacy.tokens.doc.Doc)
