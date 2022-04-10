# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# 78 65 89 86 55 91 64 89
# The highest score in the class is: 91

# Think about the logic before writing code.
#  How can you compare numbers against each other
#  to see which one is larger?
highestscore = 0
for currentscore in student_scores:
    if currentscore > highestscore:
        highestscore = currentscore

print("\n----------------------------------------")
print(f"Highest Score in the class is: {highestscore}")    
print("----------------------------------------\n")

# fast way
# print(max(student_scores))
# print(min(student_scors))