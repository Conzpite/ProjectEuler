import math

primeSet = set()
primeSet.add(2)

#Can skip any even numbers, or any numbers with even digits in it
for i in range(3, 1000000, 2):
    if i in primeSet:
        continue

    #Check if there is even digit
    tmp = i
    evenFound = False
    digitArr = []
    while tmp > 0:
        if tmp % 2 == 0:
            evenFound = True
            break
        digitArr.append(tmp % 10)
        tmp //=10

    if evenFound:
        continue


    nonPrimeFound = False
    cycleList = []

    digitsNum = len(digitArr)
    for cycle in range(0, digitsNum):
        num = 0
        for digits in range(0, digitsNum):
            num *= 10
            num += digitArr[(cycle+digits) % digitsNum]

        cycleList.append(num)

    for cycle in cycleList:
        #check if number is a prime
        isPrime = True
        sqRt = round(math.sqrt(cycle))

        for j in range(3, sqRt + 1, 2):
            if cycle % j == 0:
                isPrime = False
                break
        
        if not isPrime:
            nonPrimeFound = True
            break

    if not nonPrimeFound:
        primeSet.update(cycleList)


print(len(primeSet))
