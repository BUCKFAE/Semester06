def ListCreate():
    # Code of the empty list 
    return 2

def ListGetLength(l):
    # l is a decimal number -> l needs to be converted to binary
    # If l does not start with 10 something went wrong
    # If bit i, i + 1 is 10 -> found a divider
    start = 2

    length = 0

    while(start <= (binLength(l))):
        if binTestBit(l, start) == 0:
            if binTestBit(l, start + 1) == 1:
                length = length + 1
        start = (start + 2)

    return length

def ListGetElement(l, i):
    return 0

def ListAppendElement(l, e):

    # Appending len(bin(e)) bits to the right
    l = prodZ(l, powZ(2, (binLength(e) * 2) + 2))
    
    # Stores the number with bits doubled
    ee = 0

    # Current index of bit we need to double
    counter = binLength(e)

    # Doubling all bits
    while (counter >= 0):
        if (binTestBit(e, counter) == 1):
            # Doubling Bit
            ee = ee + powZ(2, prodZ(counter, 2))
            ee = ee + powZ(2, (prodZ(counter, 2) + 1))
        counter -= 1

    # Shifting ee by two to be able to append 10
    ee = prodZ(ee, prodZ(2, 2))

    # Adding divider in front of ee
    l = l + 2

    # Appending ee to the list
    l = (l + ee)

    # Returning the list
    return l

def binLength(n):
    l = 1
    while (powZ(2, l) <= n):
        l = (l + 1)
    return l

def binTestBit(n, i):
    # If n >= 0 and 1 <= i <= |bin(n)|: returns the nth bit

    result = 1

    counter = 0

    # Dividing by two is equal to a bitshift by one
    while (counter < i):
        n = divZ(n, 2)
        counter = (counter + 1)

    # Testing if the number is odd or
    if (prodZ(divZ(n, 2) , 2) == n):
        result = 0

    return result

def powZ(x, y):
    res = 1
    counter = 0
    while (counter < y):
        res = prodZ(res, x)
        counter = (counter + 1)
    
    return res


def prodZ(x, y):

    # Initialisierung
    [i, z] = [0, 0]

    # Negatives Vorzeichen von x entfernen
    if (x < 0):
        x = (0 - x)
        y = (0 - y)

    # x-mal y auf z addieren 
    for i in range(0, x):
        z = (z + y)

    # z zurück geben
    return z


def divZ(x, y):
    if (y != 0):

        # If y is negative, move the sign from x to y
        # If this is not done prodZ(y, z) would get
        # smaller (more negative) the bigger z is
        if (y < 0):
            y = (0 - y)
            x = (0 - x)
        
        z = 0
        
        # If x is negative z has to be as well in 
        # order for prodZ(y, z) to be able to
        # produce negative numbers
        if (x < 0):
            z = x

        # Finding tge samallest z with
        # y * z <= x
        while (prodZ(y, z) <= x):
            z = (z + 1)

        # Correcting as we incremented z to far
        z = (z - 1)

    # Returning the result, will be undefined if 
    # y is zero
    return z