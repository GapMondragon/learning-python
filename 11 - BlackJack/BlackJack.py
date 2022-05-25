from dataclasses import replace
import random
playerCards = []
computerCards = []

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

for x in range(2):
    playerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))

playerSum = sum(playerCards)
computerSum = sum(computerCards)
comHiddenCard = []

comHiddenCard = computerCards
comHiddenCard[1] = "X"

def playerPhaseShowCards():
    playerSum = sum(playerCards)
    print("\n-----------------\n")
    print(f"Player has: {playerCards}")
    print(f"Total: {playerSum}")
    print(f"Computer has: {computerCards}")
    # print(f"Total: {computerSum}")
    print("-----------------\n")


def initialDrawVerdict():
    if computerSum == 21:
        print("Computer has BlackJack. Computer Wins!")
    if playerSum == 21:
        if computerSum == 21:
            print("Draw!")
        else:
            print("Player Wins!")



def aceCheck(playercomputer):
    currentCards = (playercomputer)
    replaceAceContinue = True
    while replaceAceContinue:
        i = 0
        if currentCards[i] == 11:
            currentCards[i] = 1
            replaceAceContinue = False
        i += 1
    print(currentCards)

def drawCardPlayerPhase():
    anotherCard = input("Do you want another card? y or n \n")
    if anotherCard == "y":
        playerCards.append(random.choice(cards))
        playerSum = sum(playerCards)
        playerPhaseShowCards()
        if playerSum > 21:
            print("Over 21! You Lose. :p")
        else:
            drawCardPlayerPhase()

playerPhaseShowCards()
initialDrawVerdict()
drawCardPlayerPhase()





