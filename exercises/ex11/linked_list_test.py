"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730607960"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Last of an empty Linked List should raise a IndexError."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3)


def test_value_at_0_index() -> None:
    """Should return the data of the first head."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_non_0_index() -> None:
    """Should return data at any non empty head."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_max_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_ascending() -> None:
    """Should return the data of the first head."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_descending() -> None:
    """Should return the data of the first head."""
    linked_list = Node(30, Node(20, Node(10, None)))
    assert max(linked_list) == 30


def test_max_ascending_and_descending() -> None:
    """Should return the data of the first head."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_linkify_empty() -> None:
    """Linkify of an empty Linked List should raise a IndexError."""
    assert linkify([]) is None


def test_linkify_ascending() -> None:
    """Tests with an asceding list."""
    assert str(linkify([1, 2, 3])) == "1 -> 2 -> 3 -> None"


def test_linkify_descending() -> None:
    """Tests with a desceding list."""
    assert str(linkify([3, 2, 1])) == "3 -> 2 -> 1 -> None"


def test_scale_descending() -> None:
    """Tests with a desceding list."""
    assert str(scale(linkify([3, 2, 1]), 2)) == "6 -> 4 -> 2 -> None"


def test_scale_ascending() -> None:
    """Tests with an asceding list."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"