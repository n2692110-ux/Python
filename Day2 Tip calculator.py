# Welcome to TIP CALCULATOR

bill = float(input("What was your bill ?  "))
tip = int(input("How much tip did you like to give ? 10%,12%,14% : "))
people = int(input("How many people to split the bill?"))

tip_value = tip / 100

total_tip = tip_value * bill

total_bill = ((total_tip + bill)/ people)

print("Your total bill is:", total_bill)






