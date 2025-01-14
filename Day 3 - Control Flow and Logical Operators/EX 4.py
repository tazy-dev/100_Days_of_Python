#Pizza Order
print("Welcome To Python Pizza Delivery")
size = input("What size do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
add_cheese = input("Do you want cheese? Y or N? ")

total_bill = 0
if (size == "S"):
    total_bill+=15
    if add_pepperoni =="Y":
        total_bill+=2
else:
    
    if add_pepperoni =="M":
        total_bill+=20
    else:
        total_bill+=25
    if add_pepperoni =="Y":
        total_bill+=3
if add_cheese =="Y":
        total_bill+=1

print(f"Your final bill is ${total_bill}")