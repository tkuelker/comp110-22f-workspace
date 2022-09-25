"""bsdafads."""


def change_and_check(x: int, nums: list[int]) -> int:
    """L."""
    if x < 0:
        return 0
    
    i: int = 0
    while i < len(nums):
        nums[i] += x
        i += 1

    i: int = 0
    while i < len(nums):
        if nums[i] == x:
            return 0
        i += 1
    
    return x - 1

def main() -> None:
    """The entery point."""
    num_1: int = 0
    list_1: list[int] = [1, 2, num_1]
    list_1.append(change_and_check(2, list_1))
    list_1.append(change_and_check(3, list_1))
    print(list_1)


main()
