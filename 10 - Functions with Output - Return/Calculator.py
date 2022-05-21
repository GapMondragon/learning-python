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
    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))

        # e.g. * .... calculation_function = multiply
        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1,num2)

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. \n: ") == ("y"):
            num1 = answer
        else:
            should_continue = False
            # recursion
            calculator()

calculator()