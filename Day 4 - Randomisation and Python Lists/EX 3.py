import random as rnd


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
print(f"{row1}\n{row2}\n{row3}\n")
map = [row1,row2,row3]
pos = input("Where Do you want to bury the treasure :\n")
first_index = int(pos[1]) -1
second_index = int(pos[0]) -1
map[first_index][second_index]= "X"
print(f"{row1}\n{row2}\n{row3}\n")
