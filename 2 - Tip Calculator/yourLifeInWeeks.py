# ask for age
# calculate how mande days, weeks, and months left to live if you live up to 90

# 1 year is 365 days | 52 weeks | 12 months

age = input("What is your current age? ")
# convert age to float since it is a string
yearsFloat = float(90 - float(age))
days = yearsFloat * 365 
weeks = yearsFloat * 52
months = yearsFloat * 12

# convert to int for better presentation
years = int(yearsFloat)
days = int(days)
weeks = int(weeks)
months = int(months)

print(f"You have {years} years or {months} months or {weeks} weeks or {days} days left if you live up to 90.")