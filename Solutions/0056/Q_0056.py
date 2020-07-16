import math
import time

def main():
    maxDigitalSum = 0
    for a in range(0,100):
        for b in range(0,100):
            digitalSum = 0
            num = a ** b

            while num > 0:
                digitalSum += num % 10
                num //= 10

            maxDigitalSum = max ( maxDigitalSum, digitalSum)

    print(maxDigitalSum)
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

