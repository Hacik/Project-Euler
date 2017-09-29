# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse_int(n):
    return int(str(n)[::-1])

def palindrome():
    full_list = []
    filters = []
    lowest_number = 100
    max_number = 999
    for x in range(lowest_number, max_number+1):
        for y in range(lowest_number, max_number+1):
            full_list.append(x*y)
    for n in full_list:
        if int(n) == reverse_int(n):
            filters.append(n)
    print(max(filters))


palindrome()
