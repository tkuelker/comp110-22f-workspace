"""EX04 - 'list' Utility Functions."""


def all(all_ints: list[int], search_int: int) -> bool:
    """Checks if all ints in a list match the indicated int."""
    i: int = 0
    if len(all_ints) == 0:
        return False
        # returns false if the list all_ints is empty.
    else:
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
    max_int: int
    i: int = 0
    b: int = 0
    if len(input) == 1:
        max_int = input[0]
        return max_int
        # returns the only int as max_int if the list only has one int.
    else:
        while i < len(input) and b < len(input):
            if input[i] >= input[b]:
                max_int = input[i]
                b += 1
            else:
                max_int = input[b]
                i = b
                b = 0
                # sets i equal to b and resets the value of b to 0 if a new max_int is found. This allows for the new max_int to be checked against every index until either a new index is found of the while loop conditions are not longer met.
        return max_int


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Checks if lists are identical."""
    i: int = 0
    if len(list_a) != len(list_b):
        return False
    elif len(list_a) == 0:
        return True
    else:
        while i < len(list_a):
            if list_a[i] != list_b[i]:
                return False
            else:
                i += 1
        return True
    

__author__ = "730609760"
