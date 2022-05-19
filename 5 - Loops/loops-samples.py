fruits = ["Apple", "Peach", "Pear"]
print(fruits)

print("-----")

# foreach fruit in list(fruits)
# no need print(f"..") or {} because ara na siya sulod for loop
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print("-----")


# range
# range(start,stop,step)
# from number , end sa 10 but excluding 10,
#  count every 3 steps so ang gwa is 1 _ _ 4 _ _ 7 _ _ 
for number in range(1, 10, 3):
    print(number)

print("-----")

# add 1+2+3+4...100, excluding 101
total = 0
for number in range(1, 101):
    total += number
print(total)

print("-----")