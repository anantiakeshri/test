#Love Calculator game
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

joined_name = name1 + name2
lower_string = joined_name.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t + r + u + e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l + o + v + e

love_calculator = int(str(true) + str(love))

if (love_calculator < 10) or (love_calculator > 90):
    print(f"Your score is {love_calculator}, you go together like coke and mentos.")
elif (love_calculator >= 40) and (love_calculator <= 50):
    print(f"Your score is {love_calculator}, you are alright together.")
else:
    print(f"Your score is {love_calculator}.")
