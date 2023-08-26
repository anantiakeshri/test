# Black Jack mmini game - code in python. BY Anantia Keshri
# Link to play this original game -  https://games.washingtonpost.com/games/blackjack/

import random
import os
from BlackJack_art import text

start = print("Let's start the game.")

## The deck is unlimited in size. There are no jokers. 
## The Jack/Queen/King all count as 10. The the Ace can count as 11 or 1.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
# 0 will represent a blackjack in our game
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
    # You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. 
# If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. 
# If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Both you and opponent went over."
    
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "You lose, Opponent has Black Jack."
    elif user_score == 0:
        return "You win, with a Black Jack."
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, you win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Opponent win."

def play_game():
    #Deal the user and computer 2 cards each using deal_card() and append().  
    print(text)

    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"    Your cards: {user_card}, current score: {user_score}.")
        print(f"    Computer's first card {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        # If the game has not ended, ask the user if they want to draw another card. 
        # If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            ask = input("   Draw another card? Type 'Y' to get another card or 'N' to pass: ").lower()
            if ask == "y":
                user_card.append(deal_card())
            else:
                game_over = True
                
    # Once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long as it has a score less than 17.           
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"    Your final hand: {user_card}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play_game()