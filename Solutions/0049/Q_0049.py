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

answer = ""
answerFound = False

primeList = []
checkedNumSet = set([1487, 4817, 8147])

for i in range(1000, 10000):
    if IsPrime(i):
        primeList.append(i)

for prime in primeList:
    if i in checkedNumSet:
        #skip numbers that are already checked
        continue

    digitList = [x for x in str(prime)]
    permutations = list(itertools.permutations(digitList))

    acceptedNums = []
    for p in permutations:
        num = int(p[0]) * 1000 + int(p[1]) * 100 + int(p[2]) * 10 + int(p[3])

        if num in checkedNumSet or num not in primeList:
            #skip numbers that are already added or not prime
            checkedNumSet.add(num)
            continue

        checkedNumSet.add(num)
        acceptedNums.append(num)

    if len(acceptedNums) < 3:
        continue

    combis = itertools.combinations(acceptedNums, 3)
    for combo in combis:
        l = list(combo)
        list.sort(l)

        if(l[1] - l[0] == l[2] - l[1]):
            answerFound = True
            answer += str(l[0]) + str(l[1]) + str(l[2])

    if answerFound:
        break

print(answer)

print("--- %s seconds ---" % (time.time() - start_time))
