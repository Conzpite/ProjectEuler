import math
import sys

def PentagonalNumber(n):
    return n * (3*n-1) // 2


def IsPentagonal(num):
    '''
    From Pn = n(3n - 1) / 2
    we can get 3n^2 - n - 2Pn = 0
    Solving for n using quadratic equation, we get
    n = (1 +- sqrt(1 + 24Pn))/ 6
    We can ignore the negative portion due to n being positive integers
    '''
    n = (1.0 + math.sqrt(1 + 24 * num)) / 6.0
    return int(n) == n


smallestD = sys.maxsize
foundAnswer = False
checkedN = 1

'''
To be honest, I am not sure how to prove that the answer is the smallest 
possible answer, but here I just used the first(and thus most likely smallest answer) to turn up
'''
while not foundAnswer:
    a = PentagonalNumber(checkedN)
    for bN in range(1, checkedN):
        b = PentagonalNumber(bN)

        if a - b < smallestD and IsPentagonal(a-b):
            tmpSum = a + b

            if IsPentagonal(tmpSum):
                foundAnswer = True
                smallestD = a - b

    checkedN += 1

print(smallestD)

