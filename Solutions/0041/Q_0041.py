import math
from itertools import permutations

def IsPrime(num):
    if num <= 1:
        return False

    sqRt = round(math.sqrt(num))
    for i in range(2, sqRt + 1):
        if num % i == 0:
            return False
    return True

largest = 0

#Start with the highest number (9) and moves down, skipping 
#short pandigital primes
highestDigit = 9
while largest == 0 and highestDigit >= 1:
    l = list(permutations(range(1, highestDigit + 1)))

    for permutation in l:
        num = 0
        for i in permutation:
            num *= 10
            num += i
        if num < largest or not IsPrime(num):
            continue
        else:
            largest = num

    highestDigit -= 1

print(largest)

