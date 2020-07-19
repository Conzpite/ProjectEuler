
import math
import time
from itertools import permutations

def GetTriangleNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n*(n+1) // 2
        n += 1
    return nums

def GetSquareNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n*n
        n += 1
    return nums

def GetPentagonalNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n*(3*n - 1)//2
        n += 1
    return nums

def GetHexagonalNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n*(2*n -1)
        n += 1
    return nums

def GetHeptagonalNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n * (5*n-3)//2
        n += 1
    return nums

def GetOctagonalNumbers():
    nums = []
    currNum = 1
    n = 1

    while currNum < 10000:
        if currNum >= 1000:
            nums.append(currNum)

        currNum = n*(3*n-2)
        n += 1
    return nums

def GetAnswer(startingTriangleNum, list1, list2, list3, list4, list5):
    startingInitialDigits = startingTriangleNum // 100
    endingDigits = startingTriangleNum % 100

    for a in list1:
        aStart = a // 100
        if aStart != endingDigits:
            continue
        aEnd = a % 100

        for b in list2:
            bStart = b // 100
            if bStart != aEnd:
                continue
            bEnd = b % 100

            for c in list3:
                cStart = c // 100
                if cStart != bEnd:
                    continue
                cEnd = c % 100

                for d in list4:
                    dStart = d // 100
                    if dStart != cEnd:
                        continue
                    dEnd = d % 100

                    for e in list5:
                        eStart = e // 100
                        if eStart != dEnd:
                            continue

                        eEnd = e % 100

                        if eEnd == startingInitialDigits:
                            return a + b + c + d + e + startingTriangleNum

    return 0

def main():
    triangleList = GetTriangleNumbers()
    squareList = GetSquareNumbers()
    pentaList = GetPentagonalNumbers()
    hexaList = GetHexagonalNumbers()
    heptaList = GetHeptagonalNumbers()
    octaList = GetOctagonalNumbers()

    specialNumbersList = [triangleList, squareList, pentaList, hexaList, heptaList, octaList]

    #Always start from a triangle number and end at the same triangle num
    #Create permutations of all possible sequence between the start and end
    tmpIndices = [1,2,3,4,5]
    indexPermutations = list(permutations(tmpIndices))

    answer = 0
    for num in triangleList:
        for permu in indexPermutations:
            answer = GetAnswer(num, specialNumbersList[permu[0]], specialNumbersList[permu[1]], specialNumbersList[permu[2]], specialNumbersList[permu[3]], specialNumbersList[permu[4]])

            if answer != 0:
                break

        if answer != 0:
            break

    print(answer)

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

