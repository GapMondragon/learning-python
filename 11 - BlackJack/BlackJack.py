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


if computerSum == 21:
    comInitialCards = computerCards
else:
    comInitialCards = []
    comInitialCards = list(computerCards)
    comInitialCards[1] = "X"

def aceCheck(playercomputerCards):
    if 11 in playercomputerCards:
        currentCards = list(playercomputerCards)
        currentCards.remove(11)
        currentCards.append(1)
        print("Print changed value of 11 to 1")
        return currentCards

def playerPhaseShowCards():
    playerSum = sum(playerCards)
    print("\n-----------------\n")
    print(f"Player has: {playerCards}")
    print(f"Total: {playerSum}")
    print(f"Computer has: {comInitialCards}")
    # print(f"Total: {computerSum}")
    print("-----------------\n")
    
    if playerSum > 21:
        newCards = aceCheck(playerCards)
        newCardsSum = sum(newCards)
        if newCardsSum > 21:
            print("BUST! OVER 21! Computer Wins!")
        else:
            drawCardComputerPhase()
    else:
        drawCardPlayerPhase()

def initialDrawVerdict():
    if computerSum == 21:
        if playerSum == 21:
            print("Push! It is a draw.")
        else:
            print("Computer has BlackJack. Computer Wins!")
    if playerSum == 21:
        if computerSum == 21:
            print("Push! It is a draw.")
        else:
            print("Player has BlackJack. You Win!")





def drawCardPlayerPhase():
    anotherCard = input("Do you want another card? \n Type 'hit' or 'stand' \n")
    if anotherCard == "hit":
        playerCards.append(random.choice(cards))
        playerPhaseShowCards()
    else:
        drawCardComputerPhase()

def drawCardComputerPhase():
    print("Computer: My turn")


playerPhaseShowCards()
initialDrawVerdict()

print("-----------------\n")



