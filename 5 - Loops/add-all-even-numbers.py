#Write your code below this row 👇

# add all even numbers from 1 - 100
total = 0
for number in range(1, 101):
    if (number % 2) == 0:
        total += number

# other way
# for number in range(2, 101, 2):
#     total += number
# print(total)

print(total)