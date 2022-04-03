print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://ascii.co.uk/art
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("---------------------------------------------")
choice = input("You are at a crosroad. Where do you want to go? \n A) Left \n B) Right? \n")
choice = choice.lower()
if choice == "a": 
    choice = input("You come across what looks like a calm river. \n A) Swim across. \n B) Use a fallen log as a bridge. \n")
    if choice == "a":
        print("The water current under the surface was very strong. You drowned. :(")
    elif choice == "b":
        print("Congrats, you made it to the other side safely.")
        choice = input("You see an abandoned house. You go inside and see 2 doors. Which one do you choose? \n A) Red Door \n B) Blue Door \n")
        if choice == "a":
            print("Congratulations! You have found the secret treasure! YOU CHOSE..... WISELY... \nNow go and spend your riches! Buy online courses and earn certifications to enhance your career. ^^")
        elif choice == "b":
            print("You entered the completely dark room. As you approached the center of the room, the door closed. \nYou hear something rattling and hissing. Suddenly you were then bitten on the leg multiple times. \nYou fell into a trap. A room filled with RattleSnakes. YOU CHOSE.... POORLY... :( Game Over")
        else:
            print("You chose none of the choices and decided to walk aimlessly on the living room. \nYou fell into a trap in the floor and was impaled by the spikes. :( Game Over")
    else:
        print("You chose none of the choices and decided to remain idle. \nA water elemental dragged you to the river and fed you to the giant goldfish. Game Over.")
elif choice == "b":
    print("You fell into a hole filled with frogs. :( Game Over. ")
else:
    print("You chose none of the choices and decided to remain idle. You were hit by a bird poop traveling at 457km/h and died.")

print("---------------------------------------------")