# Love Calculator
print("Welcome To the Love Calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

couple = name1 + name2
true_counter= couple.count("t") + couple.count("r") +couple.count("u") + couple.count("e")
love_counter= couple.count("l") + couple.count("o") +couple.count("v") + couple.count("e")

love_score = true_counter * 10 + love_counter

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else :
    print(f"Your score is {love_score}")
