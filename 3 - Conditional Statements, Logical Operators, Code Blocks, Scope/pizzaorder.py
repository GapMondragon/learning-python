
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
bill = 0

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1

if size == "S" or size == "s":
    bill += 15
    sizeWord = "Small Pizza!"
elif size == "M" or size == "m":
    bill += 20
    sizeWord = "Medium Pizza!"
elif size == "L" or size == "l":
    bill += 25
    sizeWord = "Large!"
else:
    bill += 25
    sizeWord = "Large Pizza!(Since you did not choose a correct size, we will choose for you!)"

if add_pepperoni == "Y" or add_pepperoni == "y":
    peppWord = "With pepperoni!"
    if size == "S" or size =="s":
        bill += 2
    elif size == "M" or size =="m" or size == "L" or size == "l":
        bill += 3
elif add_pepperoni == "N" or add_pepperoni == "n":
    peppWord = "Without pepperoni :("
else:
    bill += 3
    peppWord = "With pepperoni!(Since you did not choose an option, we added it for you at your cost ^^)"

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
    cheeseWord = "With cheese!"
elif extra_cheese == "N" or extra_cheese == "n":
    cheeseWord = "Without cheese :("
else:
    cheeseWord = "With cheese!(Since you did not choose from the options, we added cheese for you!"

print("------------------------------")
print("\n")
print(f"Here is what you ordered:")
print(f"{sizeWord}")
print(f"{peppWord}")
print(f"{cheeseWord}")
print(f"Your final bil is: ${bill}")
print("\n")
print("------------------------------")