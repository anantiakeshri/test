#Calculator code written by Anantia.
import os

from Calculator_art import logo, text
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": div
}

def calculator():
    print(text)
    num1 = float(input("Enter the first number: "))
    for operator in operations:
        print(operator)
        
    should_continue = True

    while should_continue:   
        operation_symbol = input("Which operation to perform? ")
        calculator_func = operations[operation_symbol]
        num2 = float(input("Enter the next number: "))
        answer = calculator_func(num1, num2)
            
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        asking =  input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ")
        if asking == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            # calculator()
            
calculator()