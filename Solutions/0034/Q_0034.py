import math

'''
Since 9! = 362,880, it is safe to say that any number above 7 digits need not be checked
'''

finalSum = 0
for i in range(10, 10000000):
    sumNum = 0
    tmp = i
    while tmp > 0:
        digit = tmp % 10
        sumNum += math.factorial(digit)
        tmp //= 10

        if sumNum > i:
            break

    if sumNum == i:
        finalSum += sumNum

print(finalSum)


