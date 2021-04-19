"""Demo on how to get the binary representation of a number"""

from typing import List

def to_binary(num: int, curr="") -> str:
    """Converts the given number n into a string representing it's binary form"""
    return str(num) if num in (0, 1) else curr + to_binary(num // 2, curr) + str(num % 2)

def to_binary_list(nums: List[int]):
    """Converts the given integers (base 10) into their list representation"""
    return int("10" + ''.join([''.join(s * 2 for s in to_binary(n)) + str(10) for n in nums]), 2)

# Ensuring to_binary function is correct
for i in range(0, 10):
    assert bin(i) == "0b" + to_binary(i)

# Ensuring to_binary_list is correct
assert to_binary_list([]) == 2
assert to_binary_list([2]) == 178
assert to_binary_list([5, 3, 2]) == 2944946
