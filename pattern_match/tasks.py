"""Task objects for each task."""
from pattern_match import models, task1


def get_tasks():
    t1 = models.Task(task1.get_goals())

    return [t1]
