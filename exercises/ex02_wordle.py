"""Wordle - practice with while loops"""

__author__ = "730471301"

"""Part 1: contains_char"""


def contains_char(word: str, letter: str) -> bool:
    assert len(letter) == 1, f"len('{letter}') is not 1"
    """determines if a letter is in word"""
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index = index + 1
    return False
