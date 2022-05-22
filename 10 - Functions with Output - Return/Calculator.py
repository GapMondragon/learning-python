from artcalculator import logo

# add
def add(n1,n2):
    return n1+n2
# subtract
def subtract(n1,n2):
    return n1-n2
# multiply
def multiply(n1,n2):
    return n1*n2
# divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# be careful of infinite loops/recursions 
# recursion (putting everything inside so that you could call it again)
def calculator():
    print(logo)

    # get first number
    num1 = float(input("What is the first number? "))

    # display symbols from dictionary as choices
    for symbol in operations:
        print(symbol)

    # while loop for continuous calculations
    should_continue = True
    while should_continue:
        
        # choose operation
        operation_symbol = input("Pick an operation: ")

        # choose 2nd number
        num2 = float(input("What is the second number? "))

        # assign the value from the dictionary depending on which key the user selected
        calculation_function = operations[operation_symbol]

        # use selected value as a function
        answer = calculation_function(num1,num2)

        # choose to proceed with while loop, to continue or not
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. \n: ") == ("y"):
            num1 = answer
        else:
            should_continue = False
            # recursion
            calculator()

calculator()