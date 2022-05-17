# dictionary = {"key":"value"}

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
123: "This is a number"}

print("\n-----Retrieve items--------------")
# Retrieve items from the dictionary
print(f" Bug: {programming_dictionary['Bug']}")
print(f" 123 number: {programming_dictionary[123]}")

print("\n-----Add New Entry--------------")
# Add new entry
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

print("\n-----Edit an Item(Bug)--------------")
# Edit an item in a dictionary
# If the item targeted does not exist, it will instead create a new item
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

print("\n-----Loop through a dictionary------")
# Loop through 
for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])

print("\n-----Create empty dictionary-------")
# Create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

print("\n---Wipe an existing dictionary--")
# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)