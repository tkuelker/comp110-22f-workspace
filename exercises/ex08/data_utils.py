"""Dictionary related utility functions."""

__author__ = "730609760"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int
    for column in table:
        n_list: list[str] = []
        i = 0
        while i < n and i < len(table[column]):
            item: str = table[column][i]
            n_list.append(item)
            i += 1
        result[column] = n_list
    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in column:
        result[item] = table[item]
    return result


def concat(y: dict[str, list[str]], x: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in y:
        result[column] = y[column]
    for column in x:
        if column in result:
            result[column] += x[column]
        else: 
            result[column] = x[column]
    return result


def count(searching: list[str]) -> dict[str, int]:
    """Produces a dict where each key is a unique value in the given list and each value associated with the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    count: int
    for item in searching:
        count = 0
        if item in result:
            count = 1
            result[item] += count
        else:
            count = 1
            result[item] = count
    return result
