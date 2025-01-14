"""
Rock Paper Scissor Game
"""
import random as rnd
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


choices = [rock,paper,scissors]

user_choice = int(input("What Do You Choose? Type 0 for rock, 1 for papper and 2 for scissors \n"))
print("You Choosed :\n")
print(f"{choices[user_choice]}\n")

comp_choice = rnd.randint(0,2)
print("Computer Choosed :\n")
print(f"{choices[comp_choice]}\n")


if(user_choice < 0 or user_choice >2):
    print("Invalid Choice : choose 0, 1 or 2")
elif(user_choice == 0 and  comp_choice == 2):
    print("You Win")
elif(user_choice == 2 and comp_choice ==0):
    print("You Lose")
elif(user_choice < comp_choice ):
    print("You Lose")
elif(user_choice > comp_choice ):
    print("You Win")
elif(user_choice == comp_choice):
    print("It's a Draw")

