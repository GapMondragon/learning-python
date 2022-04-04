# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space:\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
length_of_names_list = len(names)

# you could cheat here by setting 1 as the first value in the randint() and always putting your name first
random_number = random.randint(0,length_of_names_list - 1)
payerist = (names[random_number])

print(f"\n{payerist} will be the one to pay!! ^^")
print("\n----- Alternatively, you could use choice()-----")
altchoice = random.choice(names)
print(f"or {altchoice} could pay for it too?")