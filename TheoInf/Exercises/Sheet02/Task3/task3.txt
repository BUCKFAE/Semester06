def ListCreate():
    # Code of the empty list 
    return 2

def ListGetLength(l):
    
    # We can get the length of the list by checking how often the
    # sequence 10 appears

    # Skipping the first 10 of the list
    start = 2

    # Stores the length of the list
    length = 0

    # Checking how often the sequence 10 appears
    while(start <= binLength(l)):

        # If the current bit is 0
        if (binTestBit(l, start) == 0):
            # And the following bit is 1
            if (binTestBit(l, (start + 1)) == 1):
                # We found a word
                length = (length + 1)
        # Moving the pointer by two, as all bits are doubled
        start = (start + 2)

    # Returning the length of the list
    return length

def ListGetElement(l, i):

    # At first we search for the start and end of the given word.
    # Here we need to ensure to not forget about the dividers
    # Then we get the bits of the word one by one and add 
    # the corresponding bits to the resulting value

    # Start and End index of the word
    start = 2
    end = 2

    # Stores how many elements we've already visited
    visited = 0

    # Finding the start end end of the current word
    while (visited <= i):

        # If the current bit is 0
        if (binTestBit(l, end) == 0):
            # And the following bit is 1
            if (binTestBit(l, (end + 1)) == 1):
                # Setting the start to the word to the stop of the previous word 
                # Plus two, to account for
                if (visited == (i - 1)):
                    start = (end + 2)
                # We found a word
                visited = (visited + 1)

        # Saving the end-coordinate of the current word
        end = (end + 2)

    # We moved two to far (we counted the 10 at the end as well)
    end = (end - 2)

    # Index of the current bit
    counter = 0

    # Storing the resulting number
    result = 0

    # Storing the length of the list for offset calculation
    listLength = binLength(l)

    # Iterating over all bits
    while (counter <= (end - start)):

        # Starting at the back of the list, moving forward
        # We need the offset as binTestBit starts from the
        # last bit (farthest to the right) of the number
        bitIndex = ((listLength - end) + counter)

        # Getting the bit
        bit = binTestBit(l, bitIndex)

        # If the bit is one we append it at the front of the list
        if (bit == 1):
            result = (result + powZ(2, divZ(counter, 2)))
        
        # Moving two forward as the bits ar doubled
        counter = (counter + 2)

    # Returning the result
    return result

def ListAppendElement(l, e):

    # In order to append an element to the list, we first have to 
    # Shift the already existing bits of the list to the left. 
    # We need to shift by 2 * length(bin(n)) + 2, as all bits 
    # of the number are doubled and 10 is appended at the end

    # Shifting the list to the left to make room for the new elements
    l = prodZ(l, powZ(2, (prodZ(binLength(e), 2) + 2)))
    # Stores the number with bits doubled
    ee = 0

    # Current index of bit we need to double
    counter = binLength(e)

    # Doubling all bits of the number e
    while (counter >= 0):
        # If the current bit is one, we add 11 
        if (binTestBit(e, counter) == 1):
            # Doubling Bit
            ee = (ee + powZ(2, prodZ(counter, 2)))
            ee = (ee + powZ(2, (prodZ(counter, 2) + 1)))
        # Moving to the next bit
        counter = (counter - 1)

    # Shifting ee by two to be able to append 10
    ee = prodZ(ee, prodZ(2, 2))

    # Adding divider in front of ee
    l = (l + 2)

    # Appending ee to the list
    l = (l + ee)

    # Returning the list
    return l

def binLength(n):

    # We can get the length of the binary representation of a 
    # base-10 number by checking how often it can be divided by 2
    
    # Stores how often we were able to divide the number by 2
    result = 1

    # As long as 2 ** result is smaller than the number, we
    # increment the result
    while (powZ(2, result) <= n):
        result = (result + 1)
    
    # The result is now how often you can divide the number by 2
    return result

def binTestBit(n, i):
   
    # A right-shift can be performed by dividing the number by 20
    #
    # We shift the number n bits to the right, until the last 
    # Bit of the number is the one we are looking for
    # 
    # Then, we can check if our number is odd or even

    # Stores the result
    result = 1

    # Counts how many bit shifts we performed
    counter = 0

    # Shifting the number i - 1 times to the right
    while (counter < i):
        n = divZ(n, 2)
        counter = (counter + 1)

    # Testing if the number is odd or even
    if (prodZ(divZ(n, 2) , 2) == n):
        result = 0

    return result

def powZ(x, y):

    # Storing the result
    res = 1

    # Counting how many times we multiplied both numbers
    counter = 0

    # Multiplying res and x, y times
    while (counter < y):
        # Multiplying
        res = prodZ(res, x)
        counter = (counter + 1)
    
    # Returning the result
    return res


def prodZ(x, y):

    # Initialization
    [i, z] = [0, 0]

    # Moving negative sign form x to y
    if (x < 0):
        x = (0 - x)
        y = (0 - y)

    # Adding y x times to z
    for i in range(0, x):
        z = (z + y)

    # z Returning the result
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