
import math
import time


def CheckFor5Permutations(cubeList):
    #Store a number consisting of a count of each digit mapped to a list[smallest cube associated, number of times it appeared]
    #It should be fine even if a digit count overflow, since it remove digits, thus creating a practically new legit number
    digitsDict = {} 

    for cube in cubeList:
        digitCount = 0
        tmp = cube
        while tmp > 0:
            digit = tmp % 10
            digitCount += 10 ** digit
            tmp //= 10

        if digitCount in digitsDict:
            digitsDict[digitCount][1] += 1

            if digitsDict[digitCount][1] >= 5:
                return digitsDict[digitCount][0] 
        else:
            digitsDict[digitCount] = [cube, 1]

    return 0

def main():
    n = 1
    highestCube = 1

    digits = 1
    cubesList = []

    smallestCubeAnswer = 0
    while smallestCubeAnswer == 0:
        cubesList.clear()

        while highestCube < 10**digits:
            cubesList.append(highestCube)
            n+=1
            highestCube = n * n * n

        digits+=1
        smallestCubeAnswer = CheckFor5Permutations(cubesList)

    print (smallestCubeAnswer)

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

