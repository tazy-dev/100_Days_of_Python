"""
Determine if Prime of Not
"""
from math import ceil
def check_prime(number):
    isPrime = True
    if number == 0 or number == 1:
        isPrime = False
    elif(number > 2 and number % 2 == 0 ):
        isPrime = False
    else:
        for num in range(3, ceil(number /2 ),2):
            if number % num == 0:
                isPrime = False
                break
    if (isPrime):
        print(f"{number} is Prime")
    else :
        print(f"{number} is Not Prime")


num = int(input("Check This Number : "))
check_prime(num)