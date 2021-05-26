"""This program shows how to compute h'"""

def is_prime(x):
    return False if x < 2 else all([x % i != 0 for i in range(2, x - 1)])


def get_next_prime(x):
    x += 1
    while not is_prime(x):
        x += 1
    return x

def h(x, t):

    p = 2 
    q = 2

    for _ in range(t):
            
        if p - q == x:
            return x

        if p == q:
            q = 2
            p = get_next_prime(p)
        else:
            q += 1
    return 2

for curr in range(100):
    print(f" {curr}: {h(curr, 1000)}")