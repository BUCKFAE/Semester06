from primes import isPrime

def is_prime(x):
    return 0 if x <= 1 or any([x % i == 0 for i in range(2, int((x ** 1/ 2) + 1))]) else 1

if __name__ == '__main__':
    print(''.join(["{}: {} {}\n".format(i, is_prime(i), isPrime(i)) for i in range(20)]))
