'''
Hangman Game 
'''
import random as rnd
from  hangman_art import *
from  hangman_wordbank import Word_list
from os import system
clear = lambda: system('cls')


# Randomly Chosen Word
chosen_word = rnd.choice(Word_list)
length = len(chosen_word)
lives = 6
# The Spaces string That represent the word to be guessed
spaces =['_' for i in range( length)]
#User Guess
print(logo)
while '_'  in spaces  and  lives != 0:
    user_guess = input("Guess a letter: ").strip().lower()
    clear()
# Check if the guessed charcter is in the chosen word
    if user_guess in spaces:
        print(f"You've already guessed {user_guess}")
    elif user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        lives-=1    
    else :
        for i in range(length):
            if chosen_word[i] == user_guess:
                spaces[i] = user_guess
    print(" ".join(spaces))   
    print(HANGMANPICS[lives])
if (lives == 0):
    print("You Lose")
    print(f"The Word is {chosen_word}")
    
else :
    print("You Win")



