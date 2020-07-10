import math
from itertools import permutations 

l = list(permutations(range(0, 10)))

primeDivisor = [2,3,5,7,11,13,17]

sumNum = 0
stockLen = len(primeDivisor)
for digitsTuple in l:
    #do a trival single digit check
    if digitsTuple[3] % 2 != 0 or digitsTuple[5] % 5 != 0:
        continue

    number = 0

    #Form the whole number
    for i in range(0, 10):
        number *= 10
        number += digitsTuple[i]

    hasProperty = True
    for i in range(0, 7):
        #Slice the number accordingly, and test here
        subNumber = number
        for j in range(0, 6 - i):
            subNumber //= 10
        subNumber = subNumber % 1000
        if subNumber % primeDivisor[i] != 0:
            hasProperty = False
            break

    if hasProperty:
        sumNum += number

print(sumNum)


