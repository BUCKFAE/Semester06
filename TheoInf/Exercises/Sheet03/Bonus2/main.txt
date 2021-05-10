def prim(x):

    # Default: x is not a prime
    ret = 0

    # 0 and 1 are not prime
    if (x > 1):
        # Calling the recursive function to dertime if x is a prime
        ret = recPrim(x, 2)
    
    return ret

def recPrim(x, curr):

    # Default: x is a prime
    ret = 1

    # Exiting if curr == x
    if(curr < x):
        # If (x // curr) * curr == x
        if (prodZ(divZ(x, curr), curr) == x):
            # x is not a prime
            ret = 0
        else:
            # Checking the next number
            ret = recPrim(x, (curr + 1))

    return ret
    

def prodZ(x, y):
    # Calculates x * y using recursion instead of loops
    [ret] = [0]
    if (x < y):
        ret = prodZ(y, x)
    else:
        if (y != 0):
            ret = (x + prodZ(x, (y - 1)))
    
    return ret

def divZ(x, y):
    # Calculates x // y using recursion instead of loops
    [ret] = [0]
    if (x < y):
        ret = 0
    else:
        ret =  (1 + divZ((x - y), y))
    return ret
