# Game to randomly pick who is going to pay the bill.

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

pick_random  = len(names)

final = random.randint(0, pick_random - 1)

person_who_will_pay = names[final]

print(person_who_will_pay + " is going to buy the meal today!")