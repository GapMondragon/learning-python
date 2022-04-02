# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# use .lower() to convert all characters in string to lowercase
# use .count() to get all characters inside the string

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# convert to lowercase
name1lc = name1.lower()
name2lc = name2.lower()

# combine 2 names
namesCombined = name1lc+name2lc

# true counter
counterTRUE = 0

# love counter
counterLOVE = 0

# get TRUE total
counterTRUE += namesCombined.count("t")
counterTRUE += namesCombined.count("r")
counterTRUE += namesCombined.count("u")
counterTRUE += namesCombined.count("e")

# get LOVE total
counterLOVE += namesCombined.count("l")
counterLOVE += namesCombined.count("o")
counterLOVE += namesCombined.count("v")
counterLOVE += namesCombined.count("e")

lovemeter = str(counterTRUE) + str(counterLOVE)
# print(type(lovemeter)) = this will show that lovemeter is still str, we have to convert it to int to use on if statement
lovemeter = int(lovemeter)
# print(type(lovemeter))  now this will output lovemeter as int
print(f"{counterTRUE} + {counterLOVE} = {lovemeter}%")


print("---------------------")
if lovemeter < 10 or lovemeter > 90:
    print(f"Your Love Meter is {lovemeter}. This means that you go together like coke and mentos.")
elif lovemeter > 40 and lovemeter < 50:
    print(f"Your Love Meter is {lovemeter}. This means that you are alright together.")
else:
    print(f"Your Love Meter is {lovemeter}")

print("---------------------")
