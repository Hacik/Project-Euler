# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Brute force and exhaustive - but im tired
listB = []
for i in range(1,240000000):
    if all(i % x == 0 for x in range(1,21)):
        listB.append(i)
print(listB)
