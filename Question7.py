# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#I find going backwards hard..but we actually have to go fowards. Cool.

#QUESTION 7
def nth_prime(n, limit=125000):
    if limit % 2 != 0:
        limit += 1
    primes = [True] * limit
    primes[0],primes[1] = [None] * 2
    count = 0
    for ind,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
            count += 1
        if count == n:
            return ind
    return False

prime = nth_prime(10001)
print(prime)
