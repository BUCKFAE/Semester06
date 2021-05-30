def is_prime(x):
    return False if x < 2 else all([x % i != 0 for i in range(2, x - 1)])


def check(n):


    for p in range(2, n):

        # Skipping if p is not a prime
        if not is_prime(p):
            continue

        for q in range(2, n):
            
            # Skipping if q is not a prime
            if not is_prime(q):
                continue

            i = 1  
            j = 1

            # Increasing i and j until the result gets to big
            while (p ** i) * (q **j) <= n:

                # Checking if we found a valid solution
                if (p ** i) * (q ** j) == n:
                    return (p, q, i, j)  

                i += 1

                # Ensuring we test every valid combination of i and j
                if j == i:
                    j += 1
                    i = 1

    return None


# Valdiating results
for i in range(50):
    res = check(i)
    sol = (res[0] ** res[2]) * (res[1] ** res[3]) if not res is None else ""
    print(f"{i}: {res}: {sol}")
    