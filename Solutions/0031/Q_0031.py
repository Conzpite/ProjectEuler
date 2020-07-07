import math

#There is probably a smarter way of doing this, but the naive method will suffice here

target = 200
ways = 0
for twoHundred in range(0,2):
    for hundred in range (0,3):
        if 100 * hundred + 200 * twoHundred > target:
            break

        for fifty in range(0, 5):
            if 50 * fifty + 100 * hundred + 200 * twoHundred > target:
                break

            for twenty in range(0,11):
                if 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred > target:
                    break

                for ten in range(0, 21):
                    if 10 * ten + 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred > target:
                        break

                    for five in range(0, 41):
                        if 5 * five + 10 * ten + 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred > target:
                            break

                        for two in range (0, 101):

                            if 2 * two + 5 * five + 10 * ten + 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred > target:
                                break

                            for one in range (0, 201):

                                if 1 * one + 2 * two + 5 * five + 10 * ten + 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred == target:
                                    ways += 1
                                elif 1 * one + 2 * two + 5 * five + 10 * ten + 20 * twenty +50 * fifty + 100 * hundred + 200 * twoHundred > target:
                                    break

print(ways)
