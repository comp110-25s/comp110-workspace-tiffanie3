"""Practice with decomposing a problem into smaller subproblems to plan a tea party"""

__author__ = "730471301"


def tea_bags(people: int) -> int:
    """computes # of tea bags based on # of guests"""
    return people * 2


def treats(people: int) -> int:
    """computes the # of treats needed based on the # of teas guests are expected to drink"""
    return int(tea_bags * 1.5)
