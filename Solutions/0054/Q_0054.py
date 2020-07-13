import math
import time
from enum import IntEnum

def DebugPrint(obj):
    if False:
        print(obj)

class Rank(IntEnum):
    HIGH_CARD =  1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

def IsConsecutive(val1, val2, hasTwo):
    #Need a special condition when 2 is in the hand, since there will be a jump from the Ace to 2
    if hasTwo:
        if val1 == 2 and val2 == 11 or \
            val1 == 3 and val2 == 12 or \
            val1 == 4 and val2 == 13 or \
            val1 == 5 and val2 == 14:
            return True

    return (val1 - 2) == (val2 - 3)

#supply a sorted list of hand values (from 2 to 14)
def IsStraight(hand):
    hasTwo = hand[0] == 2

    for j in range(0, 4):
        if not IsConsecutive( hand[j], hand[j + 1], hasTwo):
            return False

    return True



#return 1 if player 1 wins, 0 otherwise
def ReadWinner(line):
    cards = line.split()

    #check if all suits are the same on either side
    playerHasFlush = [True, True]

    suitCheck = cards[0][1]
    for i in range(1,5):
        if suitCheck != cards[i][1]:
            playerHasFlush[0] = False
            break

    suitCheck = cards[5][1]
    for i in range(6,10):
        if suitCheck != cards[i][1]:
            playerHasFlush[1] = False
            break

    #Get values of cards for each player
    #For the sake of value comparision, Ace is treated as 14 
    valueMap = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14
    }
    playerHandValues = [[],[]]
    for i in range(0,5):
        value = cards[i][0]
        playerHandValues[0].append(valueMap[value])

    for i in range(5,10):
        value = cards[i][0]
        playerHandValues[1].append(valueMap[value])

    #Allocate each player hand with a score
    ranks = [Rank.HIGH_CARD, Rank.HIGH_CARD]
    tieCheck = [[], []]
    for player in range(0, 2):
        list.sort(playerHandValues[player])

        hasFlush = playerHasFlush[player]
        handValues = playerHandValues[player]
        hasStraight = IsStraight(handValues)

        if hasFlush:
            #Can only be flush, straight flush or royal flush
            if hasStraight:
                if handValues[0] == 10:
                    ranks[player] = Rank.ROYAL_FLUSH
                else:
                    ranks[player] = Rank.STRAIGHT_FLUSH
            else:
                ranks[player] = Rank.FLUSH

            #since all 5 cards are always used, just put highest values at the front
            tieCheck[player] = playerHandValues[player][::-1]
        else:
            #Can be High, 1/2 pairs, 3/4 of a kind, straight, full house
            if hasStraight:
                ranks[player] = Rank.STRAIGHT
                tieCheck[player] = handValues[::-1]
            else:
                uniqueCardValues = len(set(handValues))
                if uniqueCardValues == 5:
                    #High Card
                    ranks[player] = Rank.HIGH_CARD
                    tieCheck[player] = handValues[::-1]
                elif uniqueCardValues == 4:
                    #1 pair 
                    ranks[player] = Rank.ONE_PAIR

                    pairValue = 0
                    for i in range(0, 4):
                        if handValues[i] == handValues[i + 1]:
                            pairValue = handValues[i]
                            break
                    remainder = list(filter(lambda a: a != pairValue, handValues))
                    tieCheck[player] = [pairValue, pairValue] + remainder[::-1]
                elif uniqueCardValues == 3:
                    #3 of a kind or 2 pairs

                    pairValue1 = 0
                    pairValue2 = 0
                    for i in range(0, 4):
                        if handValues[i] == handValues[i + 1]:
                            if pairValue1 == 0:
                                pairValue1 = handValues[i]
                            else:
                                pairValue2 = handValues[i]

                    if pairValue1 == pairValue2:
                        ranks[player] = Rank.THREE_OF_A_KIND
                        remainder = list(filter(lambda a: a != pairValue1, handValues))
                        tieCheck[player] = [pairValue1, pairValue1, pairValue1] + remainder[::-1]
                    else:
                        ranks[player] = Rank.TWO_PAIR
                        remainder = list(filter(lambda a: a != pairValue1 and a != pairValue2, handValues))
                        tieCheck[player] = [pairValue1, pairValue1, pairValue2, pairValue2] + remainder[::-1]
                elif uniqueCardValues == 2:
                    #4 of a kind, full house
                    value1 = handValues[0]
                    value2 = 0
                    value1Num = 1
                    value2Num = 0

                    for i in range(1, 5):
                        if handValues[i] == value1:
                            value1Num += 1
                        else:
                            value2Num = handValues[i]
                            value2Num = 5 - value1Num
                            break

                    if value2Num > value1Num:
                        value1, value2 = value2, value1
                        value1Num, value2Num = value2Num, value1Num

                    assert(value1Num == 3 or value1Num == 4)

                    if value1Num == 3:
                        ranks[player] = Rank.FULL_HOUSE
                        tieCheck[player] = [value1, value1, value1, value2,value2] 
                    else:
                        ranks[player] = Rank.FOUR_OF_A_KIND
                        tieCheck[player] = [value1, value1, value1, value1,value2] 

    DebugPrint(playerHandValues)
    DebugPrint("Player 1: " + ranks[0].name + "   Player 2: " + ranks[1].name)
    DebugPrint("Player 1 Flush: " + str(playerHasFlush[0]) + "   Player 2 Flush: " + str(playerHasFlush[1]))

    if ranks[0].value == ranks[1].value:
        #both player have same ranking hands
        #assume one player always have a winning hand (no draws)
        DebugPrint("Close Tie")
        for j in range(0,5):
            if tieCheck[0][j] < tieCheck[1][j]:
                return 0
            elif tieCheck[0][j] > tieCheck[1][j]:
                return 1

    return ranks[0].value > ranks[1].value

start_time = time.time()

lines = []
with open("p054_poker.txt", "r") as f:
    lines = f.readlines()

player1Wins = 0
times = 1
for line in lines:
    DebugPrint("Round " + str(times))
    player1Win = ReadWinner(line)
    player1Wins += player1Win
    DebugPrint("Winner of Round " + str(times) + ": Player" + str(2 - player1Win) + "\n") 
    times += 1

print(player1Wins)
print("--- %s seconds ---" % (time.time() - start_time))
