def divtwo(x):
    ret = 0

    if (x >= 0):
        curr = 0
        while ((curr + curr) <= x):
            curr = (curr + 1)
        ret = (curr - 1)
    else:
        ret = 0
    
    return ret

def tobinary(x):

    l = []

    continueOperation = 1

    while (continueOperation == 1):

        xDivTwo = divtwo(x)

        remainder = 1

        if ((xDivTwo + xDivTwo) == x):
            remainder = 0
        
        # print(remainder)
        l.append(str(remainder))

        x = xDivTwo

        if (x == 0):
            continueOperation = 0
    
    return ''.join(l)[::-1]
    # return -1 
