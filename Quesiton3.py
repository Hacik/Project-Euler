# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

#QUESTION3
import timeit

start_time = timeit.default_timer()
elapsed = timeit.default_timer() - start_time
def max_prime_factor():
    max_number = 600851475143
    test_number = 13195
    list_of_primes = []
    for num in range(1,test_number):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
           list_of_primes.append(num)

    for i in list_of_primes:
        if test_number % i == 0:
            print(i)
    # for i in range(2, test_number+1):
    #     # print(i)
    #     if test_number % i == 0:
    #         list_of_primes.append(i)
    # print(list_of_primes[-1])
    print("Time taken:", elapsed, "seconds")




#run code
max_prime_factor()
