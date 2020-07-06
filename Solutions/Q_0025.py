import math

termPos = 2

x = 1
y = 1

div = pow(10,999)
while y // div == 0:
    tmp = x
    x = y
    y = tmp + x

    termPos = termPos + 1

print (termPos)


