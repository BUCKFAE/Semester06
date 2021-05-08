from main import a

def a_correct(n, m): 
    r = 0
    if(n == 0):     # Pos 0
        r = (m + 1)

    if((n > 0) and (m == 0)): # Pos 1
        r = a((n-1), 1) # Stored in Pos2

    if((n > 0) and (m > 0)): # Pos3
        x = a(n, (m-1)) # Calculated Pos 4
        r = a((n-1), x) # Calculated Pos5, Stored Pos6

    if((r > ((n + m) + 1))): # Pos 7
        r = (r - 1)

    return r

if __name__ == "__main__":
        for i in range(4):
            for j in range(10):
                correct = a_correct(i, j)
                actual = a(i, j)
                print("{} {}: {} {}".format(i, j, actual, correct))
                assert correct == actual
