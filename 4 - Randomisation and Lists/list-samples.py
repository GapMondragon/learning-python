fruits = ["Apple", "Watermelon", "Lychee", "Orange", "Grapes", "Mango"]

# print all data in list
print("\n-----Whole List-------------------------")
print(fruits)

# print data on index 0
print("\n-----Get 1 data [0]---------------------")
print(fruits[0])

# print data starting from the last
print("\n-----From the last use negative [-2]----")
print(fruits[-2])

print("\n-----Edit-------------------------------")
fruits[3] = "Strawberry"
print(fruits)

print("\n-----Add/Append-------------------------")
fruits.append("Kiwi")
print(fruits)

print("\n-----Add Multiple/Extend----------------")
fruits.extend(["Banana", "Raspberry", "Durian"])
print(fruits)

print("\n-----Split string to make list-----------")
stringtosplit = ("Hello,from,AskPython")
print(stringtosplit)
splittedstring = stringtosplit.split(",")
# if there is a space after the comma, you should put split(", ")
print(splittedstring)



print("-------------")
