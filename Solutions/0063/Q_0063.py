
import math
import time

def main():

    n = 1
    invalidNumberAllowence = 1000 #Make a decent assumption of the number of n that can go without finding a number that fits
    answerNum = 0
    for x in range(1, 10):
        #when x is 10, x^n will always be n + 1 digits, 10^4 = 10000 = 5 digits, etc.

        allowence = invalidNumberAllowence
        n = 1
        while allowence > 0:
            digits = math.floor(math.log10(x**n)) + 1

            if digits == n:
                answerNum += 1
            else:
                allowence -= 1
            n+=1



    print(answerNum)
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

