import math

digits = [0,1,2,3,4,5,6,7,8,9]

posToFind = 1000000
retVal = 0

for x in reversed (range(0, 10)):
    possibleCombi = math.factorial(x)

    skips = 0
    while posToFind > possibleCombi:
        posToFind -= possibleCombi
        skips = skips + 1

    retVal *= 10
    retVal += digits[skips]
    digits.pop(skips)

print(retVal)





