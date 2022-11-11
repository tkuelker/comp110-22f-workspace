"""An example of vectorized operations via operator over loading."""

from __future__ import annotations
from typing import Union

class StrArry:
    items: list[str]

    def __init__(self,items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: Union[str, StrArry]) -> StrArry:
        result: StrArry = StrArry([])
        if isinstance(rhs, str):    
            for item in self.items:
                result.items.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            i: int = 0
            while i < len(self.items):
                result.items.append(self.items[i] + rhs.items[i])
                i += 1
        return result


        

a: StrArry = StrArry(["Armondo", "Pete", "Leaky"])
b: StrArry = StrArry(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + b)
print(b + ", " + a)
