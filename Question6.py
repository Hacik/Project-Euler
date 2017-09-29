# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#squares numbers:
listA = []
for i in range(0,101):
    listA.append(i)
a = (sum(listA)**2)

#natural numbers
listB = []
for i in range(0,101):
    listB.append(i**2)
b = sum(listB)

print(a-b)
