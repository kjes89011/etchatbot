"""Interface module for tasks pattern matching and info extraction."""
from pattern_match import task1
from util import errors as err
from pattern_match.tasks import *


TASKS = {
    1: task1.goal,
    #2: task2.goal,
    #3: task3.goal,
    #4: task4.goal
}


def errors(task_number, goal_number, user_input):
    """  """
    err.check_input(user_input)
    return __task(task_number)(goal_number).errors(user_input)


def info(task_number, goal_number, user_input):
    """  """
    err.check_input(user_input)
    return __task(task_number)(goal_number).info(user_input)


def match(task_number, goal_number, user_input):
    """Public interface for pattern_match module.

    Args:
      task_number: the number of the task desired.
      goal_number: the number of the goal desired.
      user_input: SpaCy doc of the user input to process.

    Returns:
      Match object.

    Raises:
      ArgumentError: if user input is not a SpaCy doc.
    """
    err.check_input(user_input)
    return __task(task_number)(goal_number).match(user_input)


def __task(number):
    """Private interface for getting tasks by number.

    Usage from calling code:
    from pattern_match import match
    is_match, info = match.task(1).goal(1)(user_input)

    Args:
      number: the task number sought.

    Returns:
      Module containing matching code for the task. The intended
        usage is to call goal(number) on this module.

    Raises:
      InvalidKeyError: if the number passed is not in the set of
        expected task numbers.
    """
    number_of_tasks = 4
    if number not in range(number_of_tasks):
        raise err.ValueError(
            number, 'Integer in the range of 1 to %s' % number_of_tasks)
    return TASKS[number]
