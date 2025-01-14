'''
Password Generator 
'''
import random as rnd
def convert_str_to_int (string:str)-> int :
    try:
        return int(string)
    except ValueError:
        return 0
    

letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers =["0","1","2","3","4","5","6","7","8","9","0"]
symbols =['!','#','$',"%","&",'(',')','+','*']
pass_len = convert_str_to_int(input("Enter The Password Length to be generated:\n"))

sepcial_char_count = convert_str_to_int(input("Enter The number of special characters:\n"))
number_count = convert_str_to_int(input("Enter How many numbers:\n"))
char_len = pass_len -sepcial_char_count - number_count
rnd.seed(10)

password = []
for num in range(char_len):
    password.append(rnd.choice(letters))
for num in range(sepcial_char_count):
    password.append(rnd.choice(symbols))
for num in range(number_count):
    password.append(rnd.choice(numbers))
rnd.shuffle(password)
print("".join(password))


