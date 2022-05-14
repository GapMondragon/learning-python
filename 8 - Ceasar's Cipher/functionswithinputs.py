# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# function(parameter)
# value of parameter is called the argument

print("----------------")

def greet():
    print("Good morning!")
    print("Have you had your coffee?")
    print("Have a good day ahead!")

greet()

print("----------------")

def greetWithName(name):
    print(f"Good morning {name}!")
    print(f"Have you had your coffee {name}?")
    print("Have a good day ahead!")

greetWithName("Gap")

print("----------------")