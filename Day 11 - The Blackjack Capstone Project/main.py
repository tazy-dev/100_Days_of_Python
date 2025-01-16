'''
    Blackjack Capstone Project
'''


import random
from os import system as sys
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  
  if computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score == computer_score:
    return "Draw"  
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def playBlackjack():
  print(logo)

  my_cards = []
  dealer_cards = []

  for _ in range(2):
    my_cards.append(deal_card())
    dealer_cards.append(deal_card())

  while True:
    my_score = calculate_score(my_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {my_cards}, current score: {my_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if my_score == 0 or dealer_score == 0 or my_score > 21:
      break

    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
      my_cards.append(deal_card())
    else:
      break

  while dealer_score != 0 and my_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"Your final hand: {my_cards}, final score: {my_score}")    
  print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(my_score, dealer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  sys('cls')
  playBlackjack()