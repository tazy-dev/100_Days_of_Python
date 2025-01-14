print("Welcome to the Tip Calculator.")
total_bill =float(input("What was the total bill? $"))
tip_percentage =int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people =int(input("How many people to split the bill? "))

total_bill += (total_bill * tip_percentage / 100)
payment_by_person = total_bill / no_of_people 

print(f"Each Person should pay : ${round(payment_by_person,2)}")