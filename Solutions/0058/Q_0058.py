
import math
import time

def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

def main():
    currNum = 1
    sideLength = 1
    primesAtDiagonal = 0
    totalDiagonalNums = 0
    distanceToNextCorner = 2

    while totalDiagonalNums == 0 or primesAtDiagonal / totalDiagonalNums > 0.1:
        for i in range(0,4):
            currNum += distanceToNextCorner
            totalDiagonalNums += 1

            if IsPrime(currNum):
                primesAtDiagonal += 1

        sideLength += 2
        distanceToNextCorner += 2

    print(sideLength)

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

