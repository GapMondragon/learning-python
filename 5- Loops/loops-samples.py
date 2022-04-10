fruits = ["Apple", "Peach", "Pear"]
print(fruits)

print("-----")

# foreach fruit in list(fruits)
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print("-----")


# range
# range(start,stop,step)
for number in range(1, 10, 3):
    print(number)

print("-----")

# add 1+2+3+4...100
total = 0
for number in range(1, 101):
    total += number
print(total)

print("-----")