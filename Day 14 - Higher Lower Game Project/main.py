from art import logo, vs
from game_data import data
import random as rnd
import os


def get_random_account():
    return rnd.choice(data)
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
def isCorrect(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_over = False
account_b = get_random_account()
while not game_over:
    print(logo)
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
        account_b = get_random_account()
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {format_data(account_a)}\n{vs}\nCompare B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if isCorrect(guess, account_a["follower_count"], account_b["follower_count"]):
        score += 1
    else:
        game_over = True
    os.system("cls")
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")