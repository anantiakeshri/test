#Guessing the number game - Code by Anantia Keshri
import os
import random

from Number_Guess_art import logo
print(logo)

numbers = list(range(1, 101))
random_chosen_number = random.choice(numbers)

print("I'm thinking of a number between 1 to 100.")
# print(f"Pssst, the correct answer is {random_chosen_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

should_continue = False

def level_easy():
    global should_continue
    while not should_continue:
        easy_attempt = 10
        for _ in range(10):
            number_guess = int(input("Make a guess:  "))
            easy_attempt -= 1   
            if number_guess > random_chosen_number and easy_attempt != 0:
                print (f"Too high.\nGuess again.\nYou have {easy_attempt} attempt remaining.\n")
            elif number_guess < random_chosen_number and easy_attempt != 0:
                print(f"Too low.\nGuess again.\nYou have {easy_attempt} attempt remaining.\n")
            elif easy_attempt == 0 and number_guess == random_chosen_number:
                print(f"You got it right! The answer was {random_chosen_number}")
                should_continue = True
            elif easy_attempt == 0:
                print("You are out of attempt, you lose.\nBetter luck next time!")
                should_continue = True
            else:
                print(f"You got it! The answer was {random_chosen_number}.\n")  
                should_continue = True
            
def level_hard():
    global should_continue
    while not should_continue:
        hard_attempt = 5
        for _ in range(5):
            number_guess = int(input("Make a guess:  "))
            hard_attempt -= 1   
            if number_guess > random_chosen_number and hard_attempt != 0:
                print(f"Too high.\nGuess again.\nYou have {hard_attempt} attempt remaining.\n")
            elif number_guess < random_chosen_number and hard_attempt != 0:
                print(f"Too low.\nGuess again.\nYou have {hard_attempt} attempt remaining.\n")
            elif hard_attempt == 0 and number_guess == random_chosen_number:
                print(f"You got it right! The answer was {random_chosen_number}")
                should_continue = True
            elif hard_attempt == 0:
                print("You are out of attempt, you lose.\nBetter luck next time!")
                should_continue = True
            else:
                print(f"You got it! The answer was {random_chosen_number}.\n")
                should_continue = True
                
if level == "easy":
    level_easy()
elif level == "hard":
    level_hard()
else:
    print("Choose correct difficulty level.")