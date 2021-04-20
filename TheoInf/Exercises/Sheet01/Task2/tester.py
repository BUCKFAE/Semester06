from main import divtwo
from main import tobinary


def to_binary_working(num: int) -> str:
    """Converts the given number n into a string representing it's binary form"""
    return str(num) if num in (0, 1) else tobinary(num // 2) + str(num % 2)

for curr in range(0, 10):
    assert curr // 2 == divtwo(curr)

for curr in range(0, 10):
    assert to_binary_working(curr) == tobinary(curr)
