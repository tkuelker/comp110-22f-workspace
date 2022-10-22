"""Test for EX07."""

__author__ = "730609760"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_1_pair() -> None:
    """Tests use case of 1 key-value pair."""
    x: dict[str, str] = {"Lol": "Bye"}
    assert invert(x) == {"Bye": "Lol"}


def test_invert_multiple_pairs() -> None:
    """Tests use case of multiple key-value pairs."""
    x: dict[str, str] = {"Lol": "Bye", "Theo": "Kuelker", "Jeremy": "Smallson", "Boyson": "Boy"}
    assert invert(x) == {"Bye": "Lol", "Kuelker": "Theo", "Smallson": "Jeremy", "Boy": "Boyson"}


def test_invert_empty() -> None:
    """Tests edge case of an empty dict."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_favorite_color_one_color() -> None:
    """Tests use case if everyone's favorite color is the same."""
    x: dict[str, str] = {"Theo": "Green", "Abby": "Green"}
    assert favorite_color(x) == "Green"


def test_favorite_color_all_different() -> None:
    """Tests use case if noboby has the same favorite color."""
    x: dict[str, str] = {"Theo": "Green", "Abby": "Black", "Bernardo": "Beige", "Holly": "Pink"}
    assert favorite_color(x) == "Green"


def test_favorite_color_empty() -> None:
    """Test edge case of an empty list."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ""


def test_count_many_different() -> None:
    """Test use case if there are multiple unique indices."""
    x: list[str] = ["Theo", "Adam", "Thomas", "Jon"]
    assert count(x) == {"Theo": 1, "Adam": 1, "Thomas": 1, "Jon": 1}


def test_count_many_repeating() -> None:
    """Test use case if there are repeating indicies."""
    x: list[str] = ["Theo", "Adam", "Thomas", "Jon", "Theo", "Adam", "Thomas", "Jon"]
    assert count(x) == {"Theo": 2, "Adam": 2, "Thomas": 2, "Jon": 2}


def test_count_empty() -> None:
    """Test use edge case if the list if empty."""
    x: list[str] = []
    assert count(x) == {}