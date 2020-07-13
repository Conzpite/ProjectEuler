import math
import time
import itertools
import sys

def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

start_time = time.time()


primeSet = set()
checkedValues = set()

answerFound = False
answer = 0

numDigits = 2 #Total number of digits to check for
while not answerFound:
    for unknownDigitNum in range(1, numDigits):
        numOfKnownDigits = numDigits - unknownDigitNum

        minRange = 1
        maxRange = 10
        for i in range(1, numOfKnownDigits):
            minRange *= 10
            maxRange *= 10

        for number in range(minRange, maxRange):
            digitsList = [x for x in str(number)]

            for j in range(unknownDigitNum):
                digitsList.append('x')

            #quick check to see if the current sequence is already done
            if ''.join(digitsList) in checkedValues:
                continue


            combis = list(itertools.permutations(digitsList))

            for combi in combis:
                checkedValues.add(''.join(combi))

                primeFamilyNum = 0
                smallestPrimeValue = sys.maxsize
                #tmpList = []

                for replacement in range(0, 10):
                    if replacement == 0 and combi[0] == 'x':
                        continue 

                    numValue = 0
                    for char in combi:
                        numValue *= 10

                        if char == 'x':
                            numValue += replacement
                        else:   
                            numValue += int(char)

                    if IsPrime( numValue):
                        #tmpList.append(numValue)
                        primeFamilyNum+=1
                        smallestPrimeValue = min(smallestPrimeValue, numValue)

                if primeFamilyNum == 8:
                    #print(tmpList)
                    answerFound = True
                    answer = smallestPrimeValue
                    break

            if answerFound:
                break

        if answerFound:
            break


    numDigits += 1

print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
