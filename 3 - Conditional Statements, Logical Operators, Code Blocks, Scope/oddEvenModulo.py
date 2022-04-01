# The Modulo (%) operator gives you the remainder after dividing.

number = int(input("Which number do you want to check if it is odd or even? "))
remainder = number % 2

if remainder == 0:
    print(f"{number} is even. Remainder = {remainder}")

else:
    print(f"{number} is odd. Remainder = {remainder}")