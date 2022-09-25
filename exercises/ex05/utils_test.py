"""Test for EX05 Utils."""

from exercises.ex05 import utils
from utils import only_evens
from utils import sub
from utils import concat

def test_only_evens_empyt() -> None:
    """Tests an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_and_even() -> None:
    """Tests a list with a single even item."""
    xs: list[int] = [4]
    assert only_evens(xs) == [4]


def test_only_evens_many_items() -> None:
    """Tests a list with many items."""
    xs: list[int] = [7, 99, 16, 0, 19, 100, 102, 3]
    assert only_evens(xs) == [16, 0, 100, 102]


def test_concat_both_empyt() -> None:
    """Tests two empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_single_and_many() -> None:
    """Tests a list with a single item and a list with many items."""
    xs: list[int] = [0]
    ys: list[int] = [1, 5, 7, 100, -145]
    assert concat(xs, ys) == [0, 1, 5, 7, 100, -145]


def test_concat_many_and_many() -> None:
    """Tests two lists with many items."""
    xs: list[int] = [0, 600, -123, 420, 95, 9]
    ys: list[int] = [1, 77, 71, 1, -15]
    assert concat(xs, ys) == [0, 600, -123, 420, 95, 9, 1, 77, 71, 1, -15]


def test_sub_start_greater_than_end() -> None:
    """Tests when starting index is greater than ending index."""
    i_start: int = 9
    i_end: int = 2
    xs: list[int] = [9, 99, 34234]
    assert sub(xs, i_start, i_end) == []


def test_sub_start_is_0() -> None:
    """Test when starting index is 0."""
    i_start: int = 0
    i_end: int = 2
    xs: list[int] = [9, 99, 34234]
    assert sub(xs, i_start, i_end) == [9, 99]


def test_sub_start_less_than_end() -> None:
    """Tests when starting index is greater than ending index."""
    i_start: int = 1
    i_end: int = 8
    xs: list[int] = [9, 99, 34, 15, 0, 0, 3, 2, 9, 0, 22, 102,]
    assert sub(xs, i_start, i_end) == [99, 34, 15, 0, 0, 3, 2]


__author__ = "730609760"