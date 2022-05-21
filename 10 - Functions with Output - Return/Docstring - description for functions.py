# docstring
# Take a first and last name and format it to
#  return the title case version of the name
# docstring must be in the first line afterhe function declaration

f_name = input("What is your first name? ")
l_name = input("What is your Last name? ")

def format_name(f_name, l_name):
    '''Take a first and last name and format it to
     return the title case version of the name'''
    # docstring must be in the first line
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_l_name}, {formatted_f_name}"


# hover the format name in line 18
output = format_name(f_name, l_name)
print(output)