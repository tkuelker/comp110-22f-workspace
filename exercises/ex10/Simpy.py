"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

from math import sqrt

__author__ = "730609760"


class Simpy:
    """Simpy object."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructs Simpy object."""
        self.values = values

    def __repr__(self) -> str:
        """Formated print for Simpy."""
        return f"Simpy({self.values})"

    def fill(self, fill: float, num_fill: int) -> None:
        """Fills values with a specified float a specified number of times."""
        i: int = 0
        while i < num_fill:
            self.values.append(fill)
            i += 1
        while len(self.values) > num_fill:
            self.values.pop(0)
        return None

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Builds values using a range function with floats."""
        assert step != 0.0
        self.values.append(start)
        i: float = start + step
        while sqrt(i ** 2) < sqrt(stop ** 2):
            self.values.append(i)
            i += step
        return None

    def sum(self) -> float:
        """Sums a Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add method for Simpys."""
        result = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i + rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            b: int = 0
            while b < len(self.values):
                result.values.append(self.values[b] + rhs.values[b])
                b += 1
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentials method for Simpys."""
        result = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i ** rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            b: int = 0
            while b < len(self.values):
                result.values.append(self.values[b] ** rhs.values[b])
                b += 1
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equal mask creator for Simpys."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                if i == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            b: int = 0
            while b < len(self.values):
                if self.values[b] == rhs.values[b]:
                    result.append(True)
                    b += 1
                else:
                    result.append(False)
                    b += 1
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than operator for Simpys."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                if i > rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            b: int = 0
            while b < len(self.values):
                if self.values[b] > rhs.values[b]:
                    result.append(True)
                    b += 1
                else:
                    result.append(False)
                    b += 1
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator for Simpys."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            assert len(self.values) == len(rhs)
            result = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                    i += 1
                else:
                    i += 1
            return result