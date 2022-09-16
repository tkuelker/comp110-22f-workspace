"""Example implementing a lisst utility function."""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
# Gameplan:
# 1. Start with the first index
# 2. Loop through every index
#   2.A Test if item at index equal to needle
#       2.A.1 True Return True! We found it!
# 3. Return False

def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False
