"""EX05 - 'list' Utility Functions."""

def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of integers, containing only the even elements of the input parameter"""
    ys: list[int] = []
    i = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            ys.append(xs[i])
        i += 1
    return ys


def concat(xs: list[int], ys: list[int]) -> None:
    """Returns a list containing all elements of the first list, followed by all elements of the second list."""
    zs: list[int] = []
    i = 0
    while i < len(xs):
        zs.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        zs.append(ys[i])
        i += 1
    return zs


def sub(xs: list[int], i_start: int, i_end: int) -> None:
    """Returns a list which is a subset of the given list, between the specified start index and the end index - 1."""
    ys: list[int] = []
    if len(xs) == 0:
        return ys
    if i_start > len(xs):
        return ys
    if i_end <= 0:
        return ys
    if i_start < 0:
        i_start = 0
    if i_end > len(xs):
        i_end = len(xs) - 1
    while i_start < i_end:
        ys.append(xs[i_start])
        i_start += 1
    return ys


__author__ = "730609760"