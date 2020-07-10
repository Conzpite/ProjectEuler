import math

def IsSquare(num):
    sqrt = math.sqrt(num)
    return int(sqrt) == sqrt

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

primeList = []
largestPrime = 2 #can skip 2, as 2 + any 2x will always be even
largestPrime = AddPrimeToList(primeList, largestPrime, 10)

answerFound = False
answer = 0
currNum = 9

while not answerFound:
    while currNum > largestPrime:
        largestPrime = AddPrimeToList(primeList, largestPrime, 1)

    isSumOfPrimeAndTwiceSquare = False
    #Prime numbers are not composite
    if currNum not in primeList:
        for j in range(0, len(primeList)):
            if primeList[j] >= currNum:
                break
            diff = currNum - primeList[j]
            #diff will always be even, as long as 2 is ignored
            if IsSquare( diff // 2):
                isSumOfPrimeAndTwiceSquare = True
                break

        if not isSumOfPrimeAndTwiceSquare:
            answerFound = True
            answer = currNum


    currNum += 2    

print(answer)
