def decimal_binary(x: int) -> str:
    res = []
    while x != 0:
        res.append(str(x % 2))
        x //= 2
    return "0b" + ('0' if len(res) == 0 else ''.join(res[::-1]))

def binary_decimal(x: str) -> int:
    x = x[2:][::-1]
    return sum([int(x[i]) * (2 ** i) for i in range(len(x))])

def decimal_dyadic(x: int) -> str:
    res = []
    while x != 0:
        if x % 2 == 0:
            res.append("2")
            x //= 2
            x -= 2
        else:
            res.append("1")
            x //= 2
    return "2d" + ('0' if len(res) == 0 else ''.join(res[::-1]))

def dyadic_decimal(x: str) -> int:
    pass

def decimal_triadic(x: int) -> str:
    pass

def triadic_decimal(x: str) -> int:
    pass


# Testing Decimal / Binary conversion
for curr in range(100):
    print(f"{curr}: {bin(curr)}\n{binary_decimal(bin(curr))}: {decimal_binary(curr)}\n")
    assert decimal_binary(curr) == bin(curr)
    assert binary_decimal(bin(curr)) == curr

print(decimal_dyadic(109))
assert decimal_dyadic(109) == "2d212221"
assert dyadic_decimal("212221") == "109"