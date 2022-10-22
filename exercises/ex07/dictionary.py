"""EX07- Dictionary functions."""

__author__ = "730609760"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary."""
    y: dict[str, str] = {}
    for key in x:
        y[x[key]] = key
    if len(x) != len(y):
        raise KeyError("invert() arg has repeating keys.")
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Given a dictionary names and colors, returns most frequent color."""
    fav_color: str = ""
    i: int = 0
    c: int = 0
    for keys in x:
        c = 0
        for key in x:
            if x[key] == x[keys]:
                c += 1 
            if c > i:
                i = c
                fav_color = x[keys]
    return fav_color


def count(x: list[str]) -> dict[str, int]:
    """Given a list of str, returns a diction with keys of each str and values of the count of each str."""
    y: dict[str, int] = {}
    c: int = 0
    i: int = 0
    b: int = 0
    while i < len(x):
        b = 0
        c = 0
        while b < len(x):
            if x[i] == x[b]:
                c += 1
            b += 1
        y[x[i]] = c
        i += 1 
    return y