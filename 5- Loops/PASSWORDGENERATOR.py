#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pwString = ""

for x in range(0, nr_letters):
    randomletter = random.randint(0,len(letters)-1)
    pwString += (letters[randomletter])

for x in range(0, nr_symbols):
    randomsymbol = random.randint(0,len(symbols)-1)
    pwString += (symbols[randomsymbol])

for x in range(0, nr_numbers):
    randomnumber = random.randint(0,len(numbers)-1)
    pwString += (numbers[randomnumber])

print(f"\n-----Generated String------------")
print(pwString)

print(f"\n-----Make String into List-----")
StringtoList = list(pwString)
print(StringtoList)


print(f"\n-----Join List/ShuffledPW------")
random.shuffle(StringtoList)
shuffledPW = ''.join(StringtoList)
print(shuffledPW)

print("\n\n----------------------------------")