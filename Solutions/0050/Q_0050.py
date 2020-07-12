import math
import time
import itertools

def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

start_time = time.time()


primeList = []

for i in range(2, 1000000):
    if IsPrime(i):
        primeList.append(i)

highestConsecutivePrimes = 0
answer = 0

for i in range(0, len(primeList)):
    target = primeList[i]

    for startingIndex in range(0, i):
        sumNum = 0
        currIndex = startingIndex

        #just a quick counter to check when to break out early 
        maxChainCounter = 0

        while sumNum < target and currIndex < i:
            sumNum += primeList[currIndex]
            maxChainCounter+=1
            currIndex += 1

        if maxChainCounter < highestConsecutivePrimes:
            break #no way for a bigger consective primes to have a longer chain

        if sumNum == target:
            if highestConsecutivePrimes < currIndex - startingIndex:
                highestConsecutivePrimes = currIndex - startingIndex
                answer = target
                break #no way for a bigger consective primes to have a longer chain
print(answer)

print("--- %s seconds ---" % (time.time() - start_time))
