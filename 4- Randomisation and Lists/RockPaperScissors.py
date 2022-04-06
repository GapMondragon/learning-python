rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# I edited the thumb in scissors
scissors = '''
    ____
---'   _)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

fckoff = '''
(╯°□°)╯︵ ┻━┻
'''

fckoffresponse = '''
┬─┬ノ( º _ ºノ)
'''
war = '''
(╯°□°)╯︵ ┻━┻      ┬─┬ノ( º _ ºノ)
'''
memelookhehe ='''
( ͡° ͜ʖ ͡°)
'''

# ----- PLAYER -----

player = input("What do you choose?\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

# got this idea sa tutorial to make it a list. I implemented it and made my code shorter for the ascii output
choicelist = [rock,paper,scissors]

if player != "1" and player != "2" and player != "3":
    print("\n     You chose: FCK OFF!!!")
    print(fckoff)
else:
    if player == "1":
        print("\n     You chose: Rock")
    elif player == "2":
        print("\n     You chose: Paper")
    elif player == "3":
        print("\n     You chose: Scissors")
    print(choicelist[int(player)-1])
    

# ----- COMPUTER -----

# separated the player and computer to have more clear code. I could have made an if else to mix the reaction of the computer if you told it to fuckoff

import random
# get random integer between 1 and 3

if player != "1" and player != "2" and player != "3":
    print("     Computer was SHOCKED:")
    print(fckoffresponse)
else:
    random_integer = str(random.randint(1,3))
    computer = random_integer
    if computer == "1":
        print("\n     Computer chose: Rock")
    elif computer == "2":
        print("\n     Computer chose: Paper")
    elif computer == "3":
        print("\n     Computer chose: Scissors")
    print(choicelist[int(computer)-1])

print("\n\n----------\n")

if player == "1":
    if computer == "1":
        print("DRAW!")
    elif computer == "2":
        print("Computer wins!")
    elif computer == "3":
        print("You win!")
elif player == "2":
    if computer == "1":
        print("You win!")
    elif computer == "2":
        print("DRAW!")
    elif computer == "3":
        print("Computer wins!")
elif player == "3":
    if computer == "1":
        print("Computer wins!")
    elif computer == "2":
        print("You Win!")
    elif computer == "3":
        print(memelookhehe)
else:
    print(war)

print("\n----------\n")