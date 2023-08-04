#TREASURE ISLAND GAME by ANANTIA KESHRI
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
name = input("Please enter your name:\n")

choice1 = input("Which side do you want to go? Left or Right?\n").lower()

if choice1 == "left":
    choice2 = input(f'{name} you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim acorss.\n').lower()
    
    if choice2 == "wait":
        print('''
                            _  _             _  _
        .       /\\/%\       .   /%\/%\     .
            __.<\\%#//\,_       <%%#/%%\,__  .
        .    <%#/|\\%%%#///\    /^%#%%\///%#\\
            ""/%/""\ \""//|   |/""'/ /\//"//'
        .     L/'`   \ \  `    "   / /  ```
                `      \ \     .   / /       .
        .       .      \ \       / /  .
                .        \ \     / /          .
        .      .    ..:\ \:::/ /:.     .     .
        ______________/ \__;\___/\;_/\________________________________
        YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw
        ''')
        
        choice3 = input(f'{name} you\'ve arrived to the island unharmed. Which door you want to visit? Type "Blue", "Red", "Yellow" or "Green"\n').lower()
        if choice3 == "blue":
            print(f"{name} you are eaten by beasts. Game Over!")
        elif choice3 == "red":
            print(f"{name} you are burned by fire. Game Over!")
        elif choice3 == "yellow":
            print(f"Yayyy {name}, you win!")
        elif choice3 == "green":
            print(f"{name} you are stuck in Amazon Forest, be aware of wild animals.")
        else:
            print(f"{name} you chose a door that doesn't exist. Game Over!")  
               
    else:
        print(f"{name} you are attacked by angry trout. Game Over!")
        
else:
    print(f"{name} you fell into a hole. Game Over!")
