# welcome to the tip calculator
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93

totalBill = input("How much was the total bill? $")
tipPercentage = input("How much percentage tip would you like to give? %")
split = input("How many people to split the bill? ")

# get tip by getting the percentage or the totalBill
tip = float(totalBill) * (float(tipPercentage) / 100)

# add tip to totalBill
totalBillwithTip = float(totalBill) + tip

# split the bill between the people
eachShouldPay = round(totalBillwithTip / float(split),2)

print(f"Each person should pay: ${eachShouldPay}")