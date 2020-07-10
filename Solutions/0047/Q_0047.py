import math


def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

def AddPrimeToList(primeList, largestPrime, primesToAdd = 1):
    for i in range(0, primesToAdd):
        largestPrime += 1
        while not IsPrime(largestPrime):
            largestPrime += 1

        primeList.append(largestPrime)
    return largestPrime

def HasFourOrMoreDistinctPrimeFactors(num, primeList):
    primeFactors = 0

    currentPrimeIndex = 0
    latestPrimeFactor = 0
    while num > 1:
        if num % primeList[currentPrimeIndex] == 0:
            num //= primeList[currentPrimeIndex]
            if latestPrimeFactor != primeList[currentPrimeIndex]:
                primeFactors += 1
            latestPrimeFactor = primeList[currentPrimeIndex]
        else:
            currentPrimeIndex += 1

        if primeFactors >= 4:
            break


    return primeFactors >= 4


primeList = []
largestPrime = 1 
largestPrime = AddPrimeToList(primeList, largestPrime, 10)

currNum = 2

consecutiveAnswers = 0

while consecutiveAnswers < 4:
    while largestPrime < currNum:
        largestPrime = AddPrimeToList(primeList, largestPrime, 1)

    if HasFourOrMoreDistinctPrimeFactors(currNum, primeList):
        consecutiveAnswers += 1
    else:
        consecutiveAnswers = 0

    currNum+=1

print(currNum - 4)

