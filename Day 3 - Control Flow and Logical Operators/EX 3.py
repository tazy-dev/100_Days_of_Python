#Check Leap Year
year  = int(input("Enter The Year You want to Check? "))

if year % 4 == 0:
    if(year % 100 !=0 or (year % 100 ==0 and year % 400 ==0 )):
        print("Leap Year")
    else:
        print("Not leap Year")
else:
        print("Not leap Year")
