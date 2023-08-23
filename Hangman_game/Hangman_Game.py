#The Hangman Game python code - By Anantia Keshri

import random                                                   #importing library
from hangman_word import word_list

chosen_word = random.choice(word_list)                         #using choice function to pick any word at random from the list
word_length = len(chosen_word)                                 #stores len of word_list - here it is 2: [0,1,2]

#a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):                                    #for loop to iterate over the word in word_list
    display += "_"                                              #display will increment "_" number of letter in a word from word_list

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The chosen word was '{chosen_word}'")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])