# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n(put 2 digits without any comma or space)\n(Column then Row) ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# assign row and column based on the input

col = int(position[0]) - 1
row = int(position[1]) - 1
print(f"{col}, {row}")

map[row][col] = "X";


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")