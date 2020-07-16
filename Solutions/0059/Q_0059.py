
import math
import time

def main():
    asciiLetters = []
    with open("p059_cipher.txt", "r") as f:
        asciiLetters = f.readline().split(",")

    
    numericLetters = []
    for letter in asciiLetters:
        numericLetters.append(int(letter))

    plainText = ""
    textFound = False
    #Let the password be abc
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                password = [a,b,c]
                passwordLen = len(password)

                index = 0
                length = len(numericLetters)
                finalStr = ""   

                while(index < length):
                    finalStr += chr(numericLetters[index] ^ password[index % passwordLen])
                    index += 1

                #Check for presence of the most common word
                tokens = finalStr.split()
                if "the" in tokens:
                    textFound = True
                    plainText = finalStr
                    break

            if textFound:
                break

        if textFound:
            break

    #print(plainText)

    asciiSum = 0
    for char in plainText:
        asciiSum += ord(char)
    print(asciiSum)





    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

