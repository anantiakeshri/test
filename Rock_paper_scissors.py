# Rock Paper Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
your_choice = int(input('What do you want to choose? Type "0" for rock, "1" for paper and "2" for scissors. \n Your choice: '))

computer_choice = int(random.randint(0, 2))
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
  
print(f"Computer's choice: {computer_choice}")

if your_choice == 0:
  print(rock)
elif your_choice == 1:
  print(paper)
else:
  print(scissors)

if your_choice == computer_choice:
    print("Match draw.")
    
elif your_choice == 0 and computer_choice == 1:
    print("You lose.")
elif computer_choice == 0 and your_choice == 1:
    print("You win!")
    
elif your_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose.")

elif your_choice == 1 and computer_choice == 2:
    print("You lose.")
elif computer_choice == 1 and your_choice == 2:
    print("You win!")
    
else:
    print("You chose invalid number, you lose.")
    
#created by Anantia Keshri