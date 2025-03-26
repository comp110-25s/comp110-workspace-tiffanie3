__author__ = "730471301"

from exercises.ex03.dictionary import invert


def test_invert_with_letters() -> None:
    """Test use case for invert with letters"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_with_words() -> None:
    """Test use case for invert with words"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_with_empty_input() -> None:
    """Test edge case for invert with empty input"""
    assert invert({}) == {}


import pytest

with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)
