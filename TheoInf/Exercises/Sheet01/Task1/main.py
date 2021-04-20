def g(f):
    return (f + f)


def f(x):
    ret = 0
    if (x < 0):
        ret = 0
    else:
        if (x == 0):
            ret = 1
        else:
            d = g(f((x-1)))
            ret = d

    return ret
