import math

def IsBinaryPalindrome(num):
    binaryArr = []
    tracker = 1
    while tracker * 2 <= num:
        tracker *= 2
    while tracker > 0:
        if tracker <= num:
            num -= tracker
            binaryArr.append(1)
        else:
            binaryArr.append(0)

        tracker //= 2

    length = len(binaryArr)
    for index in range(0, length // 2 + 1):
        if binaryArr[index] != binaryArr[length - 1 - index]:
            return False

    return True

def IsBaseTenPalindrome(num):
    flippedNum = 0
    tmp = num
    while tmp > 0:
        flippedNum *= 10
        flippedNum += tmp % 10
        tmp //= 10

    return flippedNum == num

finalSum = 0
for i in range(1, 1000000):
    if(IsBaseTenPalindrome(i) and IsBinaryPalindrome(i)):
        finalSum += i

print(finalSum)


