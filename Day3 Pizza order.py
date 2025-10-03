#Welcome to pizza order program

print("Welcome to Python Pizza Deliveries! ")
size =input("What size pizza do you want? S,M,L : ")
pepperoni = input("How many pepperoni? Y or N : ")
extra_cheese = input("How many extra cheese? Y or N : ")

# How much they need to pay

bill =0
if size == "S":
    bill+= 10
elif size == "M":
    bill+= 15
elif size == "L":
    bill+= 20
else :
    print("Please enter a valid size")

if pepperoni == "Y":
    if size == "S":
        bill+= 5
    else:
        bill+= 10

if extra_cheese == "Y":
    if size == "S":
        bill+= 3
    else:
        bill+= 5

print(f"Your total bill is :  ${bill}.")
