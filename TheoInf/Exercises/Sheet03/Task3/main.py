def a(n, m):

    pos = [0]
    arg_n = [n]
    arg_m = [m]
    var = [0]
    
    ret = 0

    while len(pos) != 0:

        if pos[-1] == 0:
            
            # If n == 0
            if arg_n[-1] == 0:
                # r = m + 1
                var[-1] = arg_m[-1] + 1
            
            pos[-1] = 1

        elif pos[-1] == 1:

            # If n > 0 and m == 0
            if arg_n[-1] > 0 and arg_m[-1] == 0:

                # Saves next step for this layer
                pos[-1] = 2

                # a(n - 1, 1)
                pos += [0]
                arg_n += [arg_n[-1] - 1]
                arg_m += [1]
                var += [0]

            else:
                pos[-1] = 3

        elif pos[-1] == 2:
            # Stores the result of a(n - 1, 1) in r
            var[-1] += ret
            pos[-1] = 3

        elif pos[-1] == 3:
            # If n > 0 and m > 0
            if arg_n[-1] > 0 and arg_m[-1] > 0:
                pos[-1] = 4
            else:
                pos[-1] = 7

        elif pos[-1] == 4:

            # Saves next step for this layer
            pos[-1] = 5

            # a(n, m - 1)
            pos += [0]
            arg_n += [arg_n[-1]]
            arg_m += [arg_m[-1] - 1]
            var += [0]

        # Calculates a(n - 1, a(n, m - 1))
        elif pos[-1] == 5:

            # Saves next step for this layer
            pos[-1] = 6

            # a(n - 1, ret)
            pos += [0]
            arg_n += [arg_n[-1] - 1]
            arg_m += [ret]
            var += [0]

        elif pos[-1] == 6:
            # Stores the result of a(n - 1, a(n, m - 1))
            var[-1] += ret
            pos[-1] = 7

        elif pos[-1] == 7:
            # If r > n + m + 1
            if var[-1] > arg_n[-1] + arg_m[-1] + 1:
                # r = r - 1
                var[-1] = var[-1] - 1
            pos[-1] = 8
        
        else:
            # Finishing the current layer
            ret = var[-1]
            pos = pos[0: -1]
            arg_n = arg_n[0: -1]
            arg_m = arg_m[0: -1]
            var = var[0: -1]
        
    return ret