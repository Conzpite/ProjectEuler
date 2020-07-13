import math
import time


start_time = time.time()

greaterThan1MilCount = 0

for n in range(1, 101):
    nFactorial = math.factorial(n)
    if nFactorial < 1000000:
        continue

    for r in range(0, n):
        rFactorial = math.factorial(r)
        nMinusRFactorial = math.factorial(n - r)

        if nFactorial // (rFactorial * nMinusRFactorial) > 1000000:
            greaterThan1MilCount += 1

print(greaterThan1MilCount)
print("--- %s seconds ---" % (time.time() - start_time))
