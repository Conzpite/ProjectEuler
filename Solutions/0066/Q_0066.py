
import math
import time
import sys

def IsSquare(num):
    sqrt = math.sqrt(num)
    return int(sqrt) == sqrt

def DebugPrint(string):
    if False:
        print(string)

def main():
    #Solve using Chakravala method
    #See https://en.wikipedia.org/wiki/Chakravala_method#The_method

    largestX = 0
    dForLargestX = 0
    for D in range(2, 1001):
        if IsSquare(D):
            continue

        #Find a and k when b = 1, such that a^2 - D = k.
        b = 1
        a = 1
        k = a * a - D
        nextCheck = (a + 1) * (a + 1) 

        DebugPrint("D: " + str(D))
        #Try to make |k| as small as possible, but more than 0
        while abs(nextCheck - D) < abs(k):
            a += 1
            k = a * a - D
            nextCheck = (a + 1) * (a + 1) 

        absK = abs(k)
        DebugPrint("    Initial (a, b, k): (" + str(a) + ", " + str(b) + ", " + str(k) + ")")
        while k != 1:
            #Perform iterations
            #Find m such that (a + bm) // k and |m^2 - D| is minimum

            #Find possible value of m in the form xt + y = m, where t is incremented per check, and (a + bm) // k
            x = absK
            y = 1
            while  (a + b * y) % absK != 0:
                y += 1

            m = y
            minDiff = abs(m * m - D)
            nextM = x + y
            nextDiff = abs(nextM * nextM - D)

            while nextDiff < minDiff:
                m += x
                nextM += x
                minDiff = nextDiff
                nextDiff = abs(nextM * nextM - D)
            DebugPrint("    m: " + str(m))

            #Get new values of a,b and k
            newA = (a * m + D * b) // absK
            newB = (a + b * m) // absK
            newK = (m * m - D) // k

            a,b,k = newA, newB, newK
            absK = abs(k)
            DebugPrint("    New (a, b, k): (" + str(a) + ", " + str(b) + ", " + str(k) + ")")

        DebugPrint("    Final x: " + str(a))
        if a > largestX:
            largestX = a
            dForLargestX = D

    print(dForLargestX)
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

