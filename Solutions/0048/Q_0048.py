import math
import time
start_time = time.time()

sumNum = 0
for i in range(1, 1001):
    sumNum += i**i

print(sumNum % 10000000000)



print("--- %s seconds ---" % (time.time() - start_time))
