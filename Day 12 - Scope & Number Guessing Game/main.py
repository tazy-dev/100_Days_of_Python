"""
    Number Guessing Game
"""
from art import logo
from random import randint as rnd
HARDLEVELGUESS = 5
EASYLEVELGUESS = 10

def checkGuess (guess,gaol):
    if guess > goal:
        print ("Too High")
        return False
    if guess < goal:
        print ("Too Low")
        return False
    
    print (f"You got it! The Answer was {guess}.")
    return True
print(logo)

print("Welcome to The Number Guessing Game!")
print("Iam thinking of a Number Between 1 and 100")
difficulty = input("Choose a difficulty . Type 'easy' or 'hard': ")
goal = rnd(2,99)

guessesRemaining = HARDLEVELGUESS if difficulty == 'hard' else EASYLEVELGUESS
while guessesRemaining > 0:
    print(f"You have {guessesRemaining} attempts remaining to guess the number")
    guess = int(input("Make a guess : "))
    result = checkGuess(guess,goal)
    if  result :
        break
    guessesRemaining-=1
    if not result and guessesRemaining != 0:
        print ("Guess Again")
        

if guessesRemaining == 0:
    print ("You have run out if guesses, You LOSE!")
