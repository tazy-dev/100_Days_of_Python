# BMI Calculator
weight = float(input("Enter Your weight in kg: "))
Height = float(input("Enter Your height in m: "))

BMI = round((weight / Height **2),1)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
else: 
    print(f"Your BMI is {BMI}, you are clinically obese")
