height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# convert to float to be able to use operands
bmi = float(weight) / (float(height) ** 2)
# convert to string to concatenate in output
strBMI = str(bmi)

print("Your BMI is: " + strBMI)