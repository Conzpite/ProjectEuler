import math

def TriangleNumber(n):
    return n * (n+1) // 2

def IsPentagonal(num):
    '''
    From Pn = n(3n - 1) / 2
    we can get 3n^2 - n - 2Pn = 0
    Solving for n using quadratic equation, we get
    n = (1 +- sqrt(1 + 24Pn))/ 6
    We can ignore the negative portion due to n being positive integers
    '''
    n = (1.0 + math.sqrt(1 + 24 * num)) / 6.0
    return n.is_integer()

def IsHexagonal(num):
    '''
    From Hn = n(2n - 1) 
    we can get 2n^2 - n - Hn = 0
    Solving for n using quadratic equation, we get
    n = (1 +- sqrt(1 + 8Hn))/ 4
    We can ignore the negative portion due to n being positive integers
    '''
    n = (1.0 + math.sqrt(1 + 8 * num)) / 4.0
    return n.is_integer()

currTriangleN = 285

answerFound = False
answer = 0
while not answerFound:
    currTriangleN += 1

    number = TriangleNumber(currTriangleN)

    if IsHexagonal(number) and IsPentagonal(number):
        answerFound = True
        answer = number 
print(answer)
