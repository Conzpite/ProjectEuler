import math
import time

def IsLychrel(num):
    orig = num
    for i in range(0, 50):
        reverse = 0
        tmp = num

        while tmp > 0:
            reverse *= 10
            reverse += tmp % 10
            tmp //= 10

        if reverse == num:
            if i != 0:
               return False

        num += reverse
    return True

def main():
    totalLychrel = 0
    for num in range(1, 10000):
        if IsLychrel(num):
            totalLychrel += 1
    print(totalLychrel)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

