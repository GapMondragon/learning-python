# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# The average height can be calculated by adding 
# all the heights together and dividing by the 
# total number of heights. 

# **Important** You should not use the `sum()` or `len()`
#  functions in your answer.
#  You should try to replicate
#  their functionality using what you have learnt
#  about for loops.

# Example Input 
# 156 178 165 171 187

# In this case, student_heights would be a list 
# that looks like: [156, 178, 165, 171, 187]

# Example Output 
# 171

# Remember to use the round() function
# to round the average height before you print it.

counter = 0
sumofheight = 0

for height in student_heights:
    sumofheight += height
    counter += 1

averageheight = sumofheight / counter
roundedaverage = round(averageheight)

print("\n----------------------------------------")
print(f"The average height is: {roundedaverage}")

print("----------------------------------------\n")

# short way using len sum
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)