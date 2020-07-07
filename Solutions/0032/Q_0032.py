import math


'''
only 4 digits max since 1 * 9999 = 9999, which uses 9 digits at the minimum
5 digits and above would exceed the 9 digits needed and thus can be safely ignored
In addition, there are only 2 ranges to test for
    !) a is 1 digit and b is 4 digits 
    2) a is 2 digits and b is 3 digits 
Since a and b are interchangable, and any other numbers outside the above range will not result in 9 digits across the multiplicand/multiplier/product

'''

productsSet = set()
digitSet = set()
arr = [0,0,0]
for a in range (1, 100):
    bRangeLow = 100
    bRangeHigh = 1000

    if a < 10:
        bRangeLow =1000
        bRangeHigh=10000

    for b in range(bRangeLow, bRangeHigh):
        product = a * b

        arr[0] = a
        arr[1] = b
        arr[2] = product
        totalDigits = 0

        digitSet.clear()

        duplicateDigitOrZero = False
        for i in arr:
            tmp = i
            while tmp > 0:
                totalDigits+=1
                digit = tmp % 10
                if digit == 0 or digit in digitSet:
                    duplicateDigitOrZero = True
                    break

                digitSet.add(tmp % 10)
                tmp //= 10

            if duplicateDigitOrZero  == True:
                break

        if duplicateDigitOrZero == True or totalDigits != 9:
            continue

        if len(digitSet) == 9:
            productsSet.add(product)

finalSum = 0
for num in productsSet:
    finalSum += num

print(finalSum)
