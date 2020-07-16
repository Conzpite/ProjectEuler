
import math
import time
import sys

def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

def Conjoint(num1, num2):
    digits = math.floor(math.log10(num1)) + 1
    return num2 * (10**digits) + num1

def ConcatsArePrime(num1, num2):
    joint1 = Conjoint(num1, num2)
    joint2 = Conjoint(num2, num1)

    return IsPrime(joint1) and IsPrime(joint2)

#Return list of primes
def ESieve(upperBound):
    numList = [0] * (upperBound + 1)
    primes = [2]

    for j in range(2 * 2, upperBound, 2):
        numList[j] = 1

    for i in range(3, upperBound, 2):
        if(numList[i] == 0):
            primes.append(i)

            for j in range(i * 2, upperBound, i):
                numList[j] = 1
    return primes

def main():
    primes = ESieve(10000)

    answerFound = False
    lowestSum = sys.maxsize

    #Impossible to create a prime by concating 2 or 5
    primes.remove(2)
    primes.remove(5)

    for a in primes:

        for b in primes:
            if a > b:
                continue

            if not ConcatsArePrime(a, b):
                continue

            for c in primes:
                if b > c:
                    continue

                if not ConcatsArePrime(a, c) or not ConcatsArePrime(b, c):
                    continue

                for d in primes:
                    if c > d:
                        continue

                    if not ConcatsArePrime(a, d) or not ConcatsArePrime(b, d) or not ConcatsArePrime(c,d):
                        continue

                    for e in primes:
                        if d > e:
                            continue 

                        if not ConcatsArePrime(a, e) or not ConcatsArePrime(b, e) or not ConcatsArePrime(c,e) or not ConcatsArePrime(d, e):
                            continue

                        validList = [a, b, c, d, e]
                        lowestSum = min(lowestSum, sum(validList))
                        answerFound = True
                        break

                    if answerFound: 
                        break

                if answerFound: 
                    break

            if answerFound: 
                break

        if answerFound: 
            break


    print(lowestSum)
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

