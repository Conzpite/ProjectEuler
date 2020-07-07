import math

'''
Since 9^5 = 59049
and 7 * 59049 = 413343 (less than 7 digits)
It is safe to say that any number with >= 7 digits can be safely ignored
'''

finalSum = 0
for i in range(2, 1000000):
    sumNum = 0
    tmp = i
    while tmp != 0:
        sumNum += pow(tmp % 10, 5)
        tmp //= 10
    if sumNum == i:
        finalSum += i

print(finalSum)
