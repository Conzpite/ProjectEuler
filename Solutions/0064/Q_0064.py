
import math
import time

def main():

    oddPeriods = 0
    for n in range(2, 10001):
        #Find closest square value < n
        i = 1
        while i * i < n:
            i += 1

        if i * i == n:
            #n is a square number, so pass
            continue

        i -= 1

        sqrtN = math.sqrt(n)

        '''Every representation of irrational square roots, is expanded to a squence of 4 numbers, a, b c and d, in the form:

         sqrt(n) = a + ________1__________
                        b + (sqrt(n) + c)//d

        '''
        #Get the initial values of a,b,c and d
        a = i

        d = n - i * i

        b = int((sqrtN + a) // d)
        c = a - d * b 

        tupleMap = {(a,b,c,d): 0} #Map tuple of (a,b,c,d) per iteration to index of the first iteration it appears in
        iteration = 1
        period = 0 #Number of digits in recurring pattern

        #print("N: " + str(n))
        #print("Iteration 0: " + str((a,b,c,d)))
        '''
        After the first calculation, a loop is created

        This goes on until a pattern occur using a, b, c and d values from previous iterations
        '''
        while True:
            a = b

            oldB = b
            oldC = c
            oldD = d

            d = (n - oldC * oldC) // oldD

            b = int((sqrtN - oldC) // d)

            c = -oldC - d * b 

            check = (a,b,c,d)
            #print("Iteration " + str(iteration) + ": " + str(check))
            if check in tupleMap:
                period = iteration - tupleMap[check]
                break
            else:
                tupleMap[check] = iteration

            iteration += 1

        #print(str(n) + "'s period: " + str(period))

        if period % 2 != 0:
            oddPeriods += 1

    print(oddPeriods)

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

