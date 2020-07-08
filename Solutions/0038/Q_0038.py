import math

'''
Since you need n > 1, the highest number than can be used is 
50,000 * (1 + 2), which breaks into the 10 digits territory, so it is safe to stop there
'''

largestResult = 0

for i in range(1, 50000):
    formedPandigital = 0

    multiplier = 1
    while formedPandigital < 100000000:
        appendix = i * multiplier
        tenMultiplier = 1

        while tenMultiplier <= appendix:
            tenMultiplier *= 10

        formedPandigital *= tenMultiplier
        formedPandigital += appendix
        multiplier += 1

    if formedPandigital >= 1000000000:
        continue

    digitSet = set()
    tmp = formedPandigital
    isPandigital = True
    while tmp > 0:
        digit = tmp % 10
        if digit == 0 or digit in digitSet:
            isPandigital = False
            break
        else:
            digitSet.add(digit)

        tmp //= 10

    if isPandigital and len(digitSet) == 9:
        if(formedPandigital > largestResult):
            largestResult = formedPandigital

print( largestResult)

