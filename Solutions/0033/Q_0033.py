import math

finalProductNumerator = 1
finalProductDenominator = 1
for a in range(10, 100):
    aTens = a // 10
    aOnes = a % 10

    #there is no way for b to be 0x, so anytime a = x0, it is either trival, or results in a fraction of 0 value, both can be ignored
    if aOnes == 0:
        continue

    #fraction must always be less than 1 in value, so a/b < 1
    for b in range(a + 1, 100):
        bTens = b // 10
        bOnes = b % 10

        fracVal = a / b

        if aOnes == bOnes and aTens < bTens:
            if aTens / bTens == fracVal:
                finalProductNumerator *= a
                finalProductDenominator *= b

        if aOnes == bTens and aTens < bOnes:
            if aTens / bOnes == fracVal:
                finalProductNumerator *= a
                finalProductDenominator *= b

        if aTens == bOnes and aOnes < bTens:
            if aOnes / bTens == fracVal:
                finalProductNumerator *= a
                finalProductDenominator *= b

        if aTens == bTens and aOnes < bOnes:
            if aOnes / bOnes == fracVal:
                finalProductNumerator *= a
                finalProductDenominator *= b

#reduce to lowest common denominator
divisor = 2
while True:
    if divisor > finalProductNumerator:
        break

    if finalProductNumerator % divisor == 0 and finalProductDenominator % divisor == 0:
        finalProductNumerator //= divisor
        finalProductDenominator //= divisor
    else:
        divisor += 1

print(finalProductDenominator)


