#  2 parameters in a function
# positional argument 
#   greet("antoine", "sweden")
# keword argument 'order doesnt affect the output'
#   greet(name="vladimir",location="russia")

def greetPositional(name,location):
    print(f"My name is {name}, I live in {location}.")

greetPositional("Antoine","Sweden")

def greetKeyword(name,location):
    print(f"My name is {name}, I live in {location}.")

greetKeyword(location="Russia", name="Vladimir")
