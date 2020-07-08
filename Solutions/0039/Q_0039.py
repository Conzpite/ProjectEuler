import math

#Create a preloaded dictionary of integer square numbers : square root
sqDict = {}

for i in range(1,1001):
    sqDict[i*i] = i

maxSolutions = 0
selectedP = 0
for p in range(1, 1001):
    solutions = 0
    for a in range (1, p):
        for b in range(a, p):   #no need to account for flipped a and b
            if a + b > p:
                #simple check to stop unneeded calculations
                break

            a2b2 = a * a + b * b
            if a2b2 in sqDict:
                c = sqDict[a2b2]
                if a + b + c == p:
                    solutions += 1
                    break #found solution for this particular a
                elif a + b + c > p:
                    #no way for the current a to get a solution
                    break

    if solutions > maxSolutions:
        selectedP = p
        maxSolutions = solutions

print (selectedP)
