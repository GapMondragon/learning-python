# Let's check if the given year is a leap year.
# Conditions
#   on every year that is evenly divisible by 4
#   EXCEPT every year that is evenly divisible by 100
#   UNLESS that year is also evenly divisible by 400

year = int(input("Which year do you want to check if it is a Leap Year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")