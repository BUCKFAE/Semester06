def f(n):

    pos = [0]
    arg = [n]
    var = [0]

    ret = 0

    # Repeating until the stack of pos is empty
    while len(pos) != 0:
        if pos[-1] == 0:        # Start of recusrion
            if arg[-1] <= 1:        # if n <= 1
                var[-1] = 1         # n = 1
                pos[-1] = 3     # Jumping to the last else
            else:
                pos[-1] = 1     # Update position
                pos += [0]      # Increase stack
                arg += [arg[-1] - 1]    # n - 1 as arg for next layer
                var += [0]
        elif pos[-1] == 1:
            var[-1] += ret
            pos[-1] = 2
            pos += [0]          # Increase stack
            arg += [arg[-1] - 2]        # n - 2 as arg for next layer
            var += [0]
        elif pos[-1] == 2:
            var[-1] += ret
            pos[-1] = 3
        else:
            # Getting the return value and popping stack
            ret = var[-1]
            pos = pos[0: -1]    # Popping from stack
            arg = arg[0: -1]
            var = var[0: -1]

    return ret

def fib(n):
    """Calculates fib(n) correctly"""
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(''.join(["{}: {} {}\n".format(i, f(i), fib(i)) for i in range(10)]))