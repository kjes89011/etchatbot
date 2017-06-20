"""Useful classes for pattern_match module."""
from util import errors as err


class ErrorResult:
    def __init__(self, has_error, errors):
        self.has_error = has_error
        self.errors = errors


class Goal:
    def __init__(self, patterns, returns_info=True):
        self.patterns = dict(zip(range(len(patterns)), patterns))
        self.returns_info = returns_info
        self.last_match = None

    def errors(self, user_input):
        # default case evaluates last call to match
        if self.last_match.is_match:
            return self.patterns[self.last_match.pattern_number]
        else:
            return ErrorResult(False, [])

    def info(self, user_input):
        # default case evaluates last call to match
        if not self.returns_info:
            return InfoResult(None, False)
        if self.last_match.is_match:
            return self.patterns[self.last_match.pattern_number]\
                .info(user_input)

    def match(self, user_input):
        for i, pattern in self.patterns:
            match_result = pattern.match(user_input)
            if match_result.is_match:
                return match_result
        return MatchResult(False, None)


class InfoResult:
    def __init__(self, info, info_expected):
        self.info = info
        self.info_expected = info_expected
        self.integrity_check()

    def integrity_check(self):
        if self.info_expected and not self.info:
            raise err.IntegrityError('Expected info but got none.')


class MatchResult:
    def __init__(self, is_match, pattern_number):
        self.is_match = is_match
        self.pattern_number = pattern_number


class Pattern:
    def __init__(self):
        pass

    def errors(self, user_input):
        raise NotImplementedError()

    def info(self, user_input):
        raise NotImplementedError()

    def match(self, user_input):
        raise NotImplementedError()


class Task:
    def __init__(self, goals):
        self.goals = dict(zip(range(len(goals)), goals))
