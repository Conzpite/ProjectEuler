
import math
import time

def main():

    termToFind = 100

    numerator = 1
    denominator = 0
    for i in reversed(range(1, termToFind + 1)):
        #work bottom up to resolve each value
        value = 2 * (i//3) if i % 3 == 0 else 1
        if i == 1:
            value = 2

        numerator, denominator = denominator, numerator
        numerator += value * denominator

    sumOfDigits = 0
    while numerator > 0:
        sumOfDigits += numerator % 10
        numerator //= 10
    print(sumOfDigits)

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

