#Question 2
def fib():
    fibonacci_numbers = [0, 1]
    filter_numbers = []
    final = []
    for i in range(2,50):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    print("Fibonnaci numbers is:", fibonacci_numbers, "\n")


    for num in fibonacci_numbers:
        if num < 4000000:
            filter_numbers.append(num)
    print("Filtered numbers is", filter_numbers)

    for i in filter_numbers:
        if i % 2 == 0:
            final.append(i)
        sum(final)
    print("Final numbers:", final, "\n", "And the sum is:", sum(final))
