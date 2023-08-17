# Coffee Machine - Code by Anantia Keshri
#Dictonary named Menu.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 3. Check for resources if it is sufficient? 
def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return f"Sorry, we don't have enough {item}."
            return False
    return True
    
    
# 4. if resource are sufficient  then ask for coins. if not sufficient resource inform.
def process_money():
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
    
    
# 5. if amount is given less don't make drink and refund money. if transaction successful. keep track of money.
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Collect your ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, the money is insufficient. Money refunded.")
        return False
    
    
# 6. make coffee
def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    
    
#1. Ask for the drink and print report
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
