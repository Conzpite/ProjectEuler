
import math
import time

def GetTriangle(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()

        triangle = []

        for line in lines:
            triangle.append( [int(x) for x in line.split() ] )
        return triangle


def main():
    #Reach the triangle bottom up and get the sum at the top
    triangle = GetTriangle("p067_triangle.txt")

    triangleRows = len(triangle)
    for row in reversed(range(1, triangleRows)):
        #Get number of elements in row above
        columns = len(triangle[row - 1])

        for col in range(0, columns):
            #Sum up the number upwards with the max value
            triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])

    #Highest Sum should be in the topmost row
    print(triangle[0][0])

    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

