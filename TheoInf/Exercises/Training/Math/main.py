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
        
