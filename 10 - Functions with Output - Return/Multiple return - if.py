# functions with output
# using Return
# putting a returned output into a variable
# output = myfunction()


f_name = input("What is your first name? ")
l_name = input("What is your Last name? ")

# turn gabriel paolo -> Gabriel Paolo
def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "Error! - either first name or last name is empty"
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_l_name}, {formatted_f_name}")
    return f"{formatted_l_name}, {formatted_f_name}"


# format_name(f_name, l_name)
output = format_name(f_name, l_name)
print(output)