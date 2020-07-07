import math

longestChainNum = 0
longestD = 0
for i in range(2,1000):
    chain = []
    isInfinite = True #if set to false, there is no recurring cycle

    '''
    Since there is only up to 1000 values,
    and fractional values are base on the denominator value
    there can only be up to 1000 unique value before it loops or ends
    so 1000 digits + a buffer should be sufficient to check for cycles
    '''
    maxDigits = 1100
    value = 1   #unit fraction
    for j in range(0, maxDigits):
        while value < i:
            value *= 10

        chain.append(value // i)
        value = value % i
        
        if value == 0:
            #no more fractional value, end
            isInfinite = False
            break

    if isInfinite == True:
        #find recurring pattern length

        #reverse so that starting non recursive stuff are ignored
        chain.reverse()

        cycle = []
        cycleFound = False
        
        cycle.append(chain[0])

        for j in range(1, len(chain)):
            if chain[j] == cycle[0]:
                #check ahead to see it is a proper cycle
                cycleLen = len(cycle)
                maxLength = cycleLen * 3
                cycleFound = True

                for k in range(0, maxLength):
                    if j + k >= maxDigits:
                        #print("Potential issue, check length of digits")
                        break

                    if cycle[k % cycleLen] != chain[j + k]:
                        cycleFound = False
                        cycle.append(chain[j])
                        break
            else:
                cycle.append(chain[j])

            if cycleFound == True:
                break

        if cycleFound and longestChainNum <= len(cycle)  :
            longestChainNum = len(cycle)
            longestD = i

print(longestD)
