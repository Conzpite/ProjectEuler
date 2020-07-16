import math
import time

def main():

    fractionsWithMoreDigits = 0

    #Record value of right hand side for use next iteration
    rightHandSideNumerator = 1
    rightHandSideDenominator = 2

    #Skip first iteration
    for i in range(2, 1001):
        newRightHandSideNumerator = rightHandSideDenominator
        newRightHandSideDenominator = 2 * rightHandSideDenominator + rightHandSideNumerator

        numerator = newRightHandSideDenominator + newRightHandSideNumerator
        denominator = newRightHandSideDenominator
        exceedingDigits = 0

        while numerator > 0:
            numerator //= 10
            exceedingDigits += 1

        while denominator > 0:
            denominator //= 10
            exceedingDigits -= 1

        if exceedingDigits > 0:
            fractionsWithMoreDigits += 1

        rightHandSideNumerator = newRightHandSideNumerator
        rightHandSideDenominator = newRightHandSideDenominator

    print(fractionsWithMoreDigits)
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

