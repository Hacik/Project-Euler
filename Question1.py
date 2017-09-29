Question 1
def mult():
    num = []
    for i in range(0,1000):
        if (i % 3 == 0 or i % 5 ==  0):
            num.append(i)
    print(num)

    b = sum(num)

    print(b)


#233168

mult()
