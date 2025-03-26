__author__ = "730471301"

from exercises.ex03.dictionary import invert


def test_invert() -> None:
    """Test use case for invert"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}
