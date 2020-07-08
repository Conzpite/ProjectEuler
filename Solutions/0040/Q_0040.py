import math

currNum = 1 #currNum to extract
remainingNum = currNum #tracks how many digits are left

currD = 1 #current digit position
targetD = 1 #position of digit to multipy to result

tenMultiplier = 1 #track the highest place of the current number

result = 1

while currD <= 1000000:
    if tenMultiplier == 0:
        currNum += 1
        remainingNum = currNum

        tenMultiplier = 1
        while tenMultiplier * 10 <= remainingNum:
            tenMultiplier *= 10

    if currD == targetD:
        result *= remainingNum // tenMultiplier
        targetD *= 10

    remainingNum = remainingNum % tenMultiplier
    tenMultiplier //= 10

    currD += 1

print(result)
