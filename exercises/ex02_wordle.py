"""Wordle - practice with while loops"""

__author__ = "730471301"

"""Part 1: contains_char"""


def contains_char(word: str, letter: str) -> bool:
    """determines if a letter (one character) is in word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index = index + 1
    return False


"""Part 2: emojified"""


def emojified(guess: str, secret: str) -> str:
    """returns a string of colored squares"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            emojis = emojis + GREEN_BOX
        else:
            if contains_char(word=secret, letter=guess[index]) == True:
                emojis = emojis + YELLOW_BOX
            if contains_char(word=secret, letter=guess[index]) == False:
                emojis = emojis + WHITE_BOX
        index = index + 1
    return emojis


"""Part 3: input_guess"""


def input_guess(n: int) -> str:
    """inputs word of n length"""
    input_word: str = input(f"Enter a {n} character word:")
    while len(input_word) != n:
        input_word = input(f"That wasn't {n} chars! Try again:")
    return input_word


"""Part 4: main"""
