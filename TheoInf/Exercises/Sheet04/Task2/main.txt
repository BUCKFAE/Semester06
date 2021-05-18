def DyadicRepresentation(x):
    # base10 to dyadic
    return [r for r in [None if i <= 0 else (1 if i % 2 == 1 else 2) for i in [eval("(" * (i * 2) + "({} - 1 // 2)".format(x) + "".join([" - 1) // 2)" for j in range(i)])) for i in range(int(x ** (1 / 2) + 1))][::-1]] if r is not None]

def Number(l):
    # Dya to base 10
    return(sum([sum([newL[i] * (2 ** i) for i in range(len(newL))]) for newL in [[v for v in l if v != 0][::-1]]]))

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

    # Return 0 if the tape contains more than one word
    if len(list(filter(None, ''.join([str(i) for i in b1]).split("0")))) > 1:
        return 0
    

    # Convert tape 1 to number
    return Number(b1)