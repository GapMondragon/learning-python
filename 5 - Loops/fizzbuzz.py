#Write your code below this row 👇

# 1-100 fizzbuzz
# # 
# `Your program should print each number from 1 to 100 in turn.` 

# `When the number is divisible by 3 
# then instead of printing the number it should print "Fizz".` 

# `When the number is divisible by 5, 
# then instead of printing the number it should print "Buzz".` 

# `And if the number is divisible by both 3 and 5 
# e.g. 15 then instead of the number it should print "FizzBuzz"`

# 1
# 2
# Fizz (3) 
# 4
# Buzz (5) 
# Fizz (6)
# 7
# 8
# Fizz (9)
# Buzz (10)
# 11
# Fizz (11)
# 13
# 14
# FizzBuzz (15)

# Remember your answer should 
# start from 1 and go up to and including 100. 
# Each number/text should be printed on a separate line.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz ({number})")
    elif number % 3 == 0:
        print(f"Fizz ({number})")
    elif number % 5 == 0:
        print(f"Buzz ({number})")
    else:
        print(number)