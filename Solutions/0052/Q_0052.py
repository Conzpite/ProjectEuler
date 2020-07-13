import math
import time


start_time = time.time()

answerFound = False
currNum = 1
nextThershold = 10
while not answerFound:
    if currNum * 6 >= nextThershold:
        #if *6 overflows the digit count, no need to check further
        currNum = nextThershold
        nextThershold *= 10
        continue

    digitsCount = 0 #Contain number of occurance for each digit (0-9)
                    #Assumes number do not go to 10 digits

    tmp = currNum
    while tmp > 0:
        digitsCount += 10 ** (tmp % 10)
        tmp //= 10

    hasSameDigits= True
    for i in range(1, 7):
        digitChecker = 0
        newNum = i  * currNum

        while newNum > 0:
            digitChecker += 10 ** (newNum % 10)
            newNum //= 10

        if digitChecker != digitsCount:
            hasSameDigits = False
            break

    if hasSameDigits:
        answerFound = True
    else:
        currNum  += 1


print(currNum)
print("--- %s seconds ---" % (time.time() - start_time))
