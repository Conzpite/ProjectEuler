import math

def IsPrime(num):
    if num <= 1:
        return False
    
    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

def HasEvenDigit(num):
    while num > 0:
        if num % 2 == 0 and num % 10 != 2: #special case as 2 is considered a prime
            return True

        num //= 10

    return False

primesFound = 0
finalSum = 0
currNum = 9

while primesFound != 11:
    currNum += 2 #Can skip any even number

    if HasEvenDigit(currNum):
        continue

    isSpecialPrime = IsPrime(currNum)
    if not isSpecialPrime:
        continue

    #Right To Left Removal Check
    tmp = currNum
    tmp //= 10 #Remove 1st digit
    while tmp > 0:

        if not IsPrime(tmp):
            isSpecialPrime = False
            break

        tmp //= 10

    if isSpecialPrime:
        #Left To Right Removal Check
        remaining = currNum
        tmp = 0

        tmp += remaining % 10
        remaining //= 10
        tenMulti = 1

        while remaining > 0:
            if not IsPrime(tmp):
                isSpecialPrime = False
                break

            tenMulti *= 10
            tmp += (remaining % 10) * tenMulti
            remaining //= 10

    if isSpecialPrime:
        primesFound += 1
        finalSum += currNum
        #print("Chosen: " + str(currNum), flush = True)

print(finalSum)

