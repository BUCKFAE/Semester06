import math

def f6(x):
    y = 0
    while x > 0:
        x = x - y - y - 1
        y = y + 1
    return y

def predict_f6(x):
    y = 0
    while x - sum([(2 * i) + 1 for i in range(0, y)]) > 0:
        y += 1
    return y

def predict_f6_2(x):
    return math.ceil(math.sqrt(x)) if x > 0 else 0

print(''.join("{}: {} {} {}\n".format(i, f6(i), predict_f6(i), predict_f6_2(i)) for i in range(0, 200)))
assert all([f6(x) == predict_f6(x) == predict_f6_2(x) for x in range(0, 200)])
