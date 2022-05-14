#Write your code below this line 👇

import math

def paint_calc(height,width, cover):
    cans = (height * width) / cover
    if cans % 2 != 0:
        cans = math.ceil(cans)
    print(f"You'll need {cans} number of cans for this.")



#Write your code above this line 👆

# Define a function called paint_calc() so that the code below works.   

# number of cans = (wall height * wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) ÷ 5
# = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# 2,4 = 2
# 3,9 = 6
# 7,13 = 19

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


