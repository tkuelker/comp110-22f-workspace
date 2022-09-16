"""EX04 - 'list' Utility Functions."""


def all(all_ints: list[int], search_int: int) -> bool:
    """Checks if all ints in a list match the indicated int."""
    i: int = 0
    while i < len(all_ints):
        if search_int != all_ints[i]:
            return False
        else: 
            i += 1
    return True


def max(input: list[int]) -> int:
    """Returns maxium value of a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_int: int = ""
    i: int = 0
    if len(input) == 1:
        max_int = input[0]
    else:
        while i < len(input) and i <= (len(input) -1):
            if input[i] < input[i + 1]:
                max_int = input[i + 1]
            else:
                max_int = input[i]
            i += 1
        return max_int


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Checks if lists are identical."""
    i: int = 0
    if len(list_a) != len(list_b):
        return False
    else:
        while i < len(list_a):
            if list_a[i] != list_b[i]:
                return False
            else:
                i += 1
            return True
    

__author__ = "730609760"
