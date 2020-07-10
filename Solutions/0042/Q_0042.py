import math

#Return highest value for comparison
def AddTriangleNumber(numSet, n):
    value = n * (n+1) // 2
    numSet.add(value)
    return value

#Set up triangle numbers by preloading some numbers
currN = 1
largestValue = 0
numSet = set()

for i in range(20):
    largestValue = AddTriangleNumber(numSet, currN)
    currN += 1

words = []
with open("p042_words.txt", "r") as f:
    words = f.readline().split(",")

triangleWordsNum = 0
for word in words:
    wordValue = 0
    wordshort = word.strip("\"")
    for char in wordshort:
        wordValue += (ord(char)- ord('A') + 1) 

    #Add more to triangle numbers to contain possible values
    while wordValue > largestValue:
        largestValue =  AddTriangleNumber(numSet, currN)
        currN += 1

    if wordValue in numSet:
        triangleWordsNum += 1

print(triangleWordsNum)
