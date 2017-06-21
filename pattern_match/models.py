"""Useful classes for pattern_match module."""
from util import errors as err


class ErrorPattern:
    def __init__(self):
        pass

    def match(self, user_input):
        raise NotImplementedError()


class ErrorResult:
    def __init__(self, has_error, error_message=None):
        self.has_error = has_error
        self.error_message = error_message


class Goal:
    def __init__(self, patterns, error_patterns, returns_info=True):
        self.patterns = dict(zip(range(len(patterns)), patterns))
        self.error_patterns = dict(zip(range(len(error_patterns)),
                                       error_patterns))
        self.returns_info = returns_info
        self.last_match = None

    def error(self, user_input):
        for i, error_pattern in self.error_patterns.items():
            error_result = error_pattern.match(user_input)
            if error_result.has_error:
                return error_result
        return ErrorResult(False, None)

    def info(self, user_input):
        # default case evaluates last call to match
        if not self.returns_info:
            return None
        if self.last_match.is_match:
            return self.patterns[self.last_match.pattern_number]\
                .info(user_input)

    def match(self, user_input):
        for i, pattern in self.patterns.items():
            match_result = pattern.match(user_input)
            if match_result:
                return True
        return False


class Match:
    def __init__(self, user_input, is_match, info):
        self.user_input = user_input
        self.match = is_match
        self.info = info


class Pattern:
    def __init__(self):
        pass

    def info(self, user_input):
        raise NotImplementedError()

    def match(self, user_input):
        raise NotImplementedError()


class Task:
    def __init__(self, goals):
        self.goals = dict(zip(range(len(goals)), goals))
