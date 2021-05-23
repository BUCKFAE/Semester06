"""This program shows how to compute f"""

def is_prime(x):
    return False if x < 2 else all([x % i != 0 for i in range(2, x - 1)])

primes = [x for x in range(1000) if is_prime(x)]

# Printing first 10 primes
print(primes[:10])

res = {}

# Testing if the numbers are in B
for curr in range(20):

    biggest_prime_index = 1

    # Searching the biggest prime that does not break the following condingion
    # p - q <= n (where q is the prime that comes before q)
    while True:
        
        # Preventing out of bounds
        assert len(primes) > biggest_prime_index 

        if (primes[biggest_prime_index] - primes[biggest_prime_index - 1]) > curr:
            break

        biggest_prime_index += 1
    

    # Checking all possible combinations
    for i in range(biggest_prime_index):

        if curr in res.keys():
            break

        for j in range(biggest_prime_index):
            if primes[i] - primes[j] == curr:
                res[curr] = (primes[i], primes[j])

# Printing the result
print(res)