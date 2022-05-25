# following this checklist
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

import random
playerCards = []
computerCards = []

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

for x in range(2):
    playerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))

playerSum = sum(playerCards)
computerSum = sum(computerCards)
print(f"Player has: {playerCards} \n Total: {playerSum}")
print(f"Computer has: {computerCards} \n Total: {computerSum}")