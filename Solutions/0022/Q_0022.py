import math

names = []
with open("p022_names.txt", "r") as f:
    names = f.readline().split(",")

names.sort()

namePos = 1
sumNum = 0
for name in names:
    nameShort = name.strip("\"")
    for char in nameShort:
        sumNum += (ord(char)- ord('A') + 1) * namePos

    namePos = namePos + 1
print(sumNum)


