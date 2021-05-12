def DyadicRepresentation(x):
    # base10 to dyadic
    #return [] if x < 1 else [2 if (x // (2 * (i))) % 2 == 0 else 1 for i in range(0, int(x ** (1 / 2)) + 1)]
    res = []

    if x < 1:
        return res


    curr = x
    while curr > 0:

        if (curr) % 2 == 0:
            curr = (curr // 2) - 1
            res += [2]
        else:
            res += [1]
            curr = (curr // 2)

    return res[::-1]


def Number(l):
    l = [i for i in l if i != 0]
    total = 0
    for exp in range(len(l)):
        num = l[len(l) - exp - 1]
        total += num * 2**exp
    return total

def GoRight(t, h):
    # Going to the right
    return t if h < len(t) - 1 else t + [0], h + 1

def GoLeft(t, h):
    # Going to the left
    return t if h != 0 else [0] + t, h - 1 if h > 0 else 0


def main(x):

    # Start state
    z = 0

    # Lists representing tapes
    b1 = DyadicRepresentation(x) + [0]
    b2 = [0]

    # Head positions
    h1 = h2 = 0 

    while (z != 1):

        if (z == 0 and b1[h1] == 1 and b2[h2] == 0):
            z = 0
            b1[h1] = 1
            b2[h2] = 1
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoLeft(b2, h2)

        elif (z == 0 and b1[h1] == 2 and b2[h2] == 0):
            z = 0
            b1[h1] = 2
            b2[h2] = 2
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoLeft(b2, h2)

        elif (z == 0 and b1[h1] == 0 and b2[h2] == 0):
            z = 2
            b1[h1] = 0
            b2[h2] = 0
            b1, h1 = b1, h1
            b2, h2 = GoRight(b2, h2)

        elif (z == 2 and b1[h1] == 0 and b2[h2] == 1):
            z = 2
            b1[h1] = 1
            b2[h2] = 0
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoRight(b2, h2)
            
        elif (z == 2 and b1[h1] == 0 and b2[h2] == 2):
            z = 3
            b1[h1] = 2
            b2[h2] = 0
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoRight(b2, h2)

        elif (z == 3 and b1[h1] == 0 and b2[h2] == 1):
            z = 3
            b1[h1] = 1
            b2[h2] = 0
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoRight(b2, h2)

        elif (z == 3 and b1[h1] == 0 and b2[h2] == 2):
            z = 3
            b1[h1] = 0
            b2[h2] = 0
            b1, h1 = GoRight(b1, h1)
            b2, h2 = GoRight(b2, h2)

        else:
            z = 1

    # Test if band contains more than one word


    # Convert band 1 to number
    return Number(b1)