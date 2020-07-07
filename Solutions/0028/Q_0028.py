import math

sumNum = 0

#add the 1 in the center
sumNum += 1

increment = 0

size = 1001

#number of 'rings' surrounding the center
rings = 1001 // 2 
value = 1

for ring in range(1, rings + 1):
    increment += 2

    #for each corner of the ring
    for i in range(0, 4):
        value += increment
        sumNum += value

print(sumNum)
