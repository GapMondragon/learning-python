# It should tell them the interpretation of their BMI
#  based on the BMI value.

# under 18.5 = underweight
# over 18.5 but below 25 = normal weight
# over 25 but below 30 = overweight
# over 30 but below 35 = obese
# above 35 = obese

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
elif bmi < 35:
    category = "obese"
else:
    category = "clinically obese"
    
print(f"Your BMI is {bmi}, you are {category}.")