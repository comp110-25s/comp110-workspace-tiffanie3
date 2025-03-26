__author__ = "730471301"

from exercises.ex03.dictionary import invert
import pytest
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color


def test_invert_with_letters() -> None:
    """Test use case for invert with letters"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_with_words() -> None:
    """Test use case for invert with words"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_with_empty_input() -> None:
    """Test edge case for invert with empty input"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_count_colors() -> None:
    """Test use case for count with colors"""
    list_colors: list[str] = ["red", "blue", "yellow", "red", "blue", "blue"]
    assert count(list_colors) == {
        "red": 2,
        "blue": 3,
        "yellow": 1,
    }


def test_count_letters() -> None:
    """Test use case for count with letters"""
    list_letters: list[str] = ["a", "b", "c", "d", "1", "a"]
    assert count(list_letters) == {"a": 2, "b": 1, "c": 1, "d": 1, "1": 1}


def test_count_empty() -> None:
    """Test edge case for count with empty list"""
    list_empty: list[str] = []
    assert count(list_empty) == {}


def test_favorite_color1() -> None:
    """Test first use case for favorite_color"""
    dict_color: dict[str, str] = {
        "Tiffanie": "blue",
        "Brandon": "blue",
        "Elena": "green",
        "Naomi": "pink",
        "Kimberly": "teal",
    }
    assert favorite_color(dict_color) == "blue"


def test_favorite_color2() -> None:
    """Test second use case for favorite_color"""
    dict_color: dict[str, str] = {
        "Bear": "black",
        "Panda": "white",
        "Capybara": "red",
        "Cow": "orange",
        "Squirrel": "yellow",
        "Coconut": "blue",
        "Violet": "purple",
        "Tapir": "red",
        "Spider": "orange",
        "Bee": "purple",
        "Monkey": "purple",
    }
    assert favorite_color(dict_color) == "purple"


def test_favorite_color3() -> None:
    """Test third use case for favorite_color"""
    dict_color: dict[str, str] = {"cat": "orange", "dog": "yellow", "guinea pig": "red"}
    assert favorite_color(dict_color) == "orange"
