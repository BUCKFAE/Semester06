correct = {}

correct[2] = True

def test_number(n: int) -> bool:
    if n in correct:
        return True

    if n % 2 == 0:
        return test_number(n // 2)
    else:
        return test_number((3 * n)  + 1)


for n in range(1, 1_000_000):

    if n % 10000 == 0:
        print(n)
    if not test_number(n):
        print(n)

print(len(correct))
