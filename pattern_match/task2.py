"""Matching input patterns for Task 2."""
from pattern_match import models
from util import test_util, errors
from pattern_match.error_patterns import errors2
from pattern_match.patterns.task2 import patterns


_goal1 = models.Goal(
    patterns=patterns.GOAL1,
    error_patterns=errors2.errors(1),
    returns_info=False)
_goal2 = models.Goal(
    patterns=patterns.GOAL2,
    error_patterns=errors2.errors(2),
    returns_info=False)
_goal3 = models.Goal(
    patterns=patterns.GOAL3,
    error_patterns=errors2.errors(3))
GOALS = {
    1: _goal1,
    2: _goal2,
    3: _goal3
}


def goal(goal_number):
    """Interface for specific goals for the task.

    Args:
      goal_number: int, indexing the goal number.

    Returns:
      Goal object, exposing subsequent interfaces.

    Raises:
      ValueError: if the goal number is invalid.
    """
    global GOALS
    number_of_goals = 6
    if goal_number not in range(number_of_goals):
        raise errors.ValueError(goal_number, 'Integer in the range (1, 6).')
    return GOALS[goal_number]


""" Testing """



