import math

finalA = -1001
finalB = -1001
longestPrimesCount = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primeCount = 0

        n = 0
        isPrime = True
        while isPrime:
            equation = n * n + n * a + b
            if equation < 1:
                isPrime = False
                break

            #check if prime
            isPrime = True
            sqRt = round(math.sqrt(equation))
            for i in range(2, sqRt + 1):
                if equation % i == 0:
                    isPrime = False
                    break

            if isPrime == True:
                primeCount += 1
                n += 1


        if primeCount > longestPrimesCount:
            longestPrimesCount = primeCount
            finalA = a
            finalB = b

print(finalA * finalB)


