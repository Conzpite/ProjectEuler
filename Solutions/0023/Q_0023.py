import math

abunNums = set()

#get all abundent numbers
for x in range(11, 28154):
    sumNum = 0
    for num in range(1, x):
        if x % num ==0:
            sumNum += num

    if sumNum > x:
        abunNums.add(x)

abunPairs = set()
for x in abunNums:
    for y in abunNums:
        abunPairs.add(x+ y)

sumRet = 0
for x in range(1, 28154):
    if x not in abunPairs:
        sumRet += x

print(sumRet)



