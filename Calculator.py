#Calculator code written by Anantia.

from Calculator_art import logo, text
print(f"{logo} {text}")

num1 = int(input("What is the first number: "))

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

for operator in operations:
    print(operator)
    
operation_symbol = input("Which operation do you want to perform? ")
calculator_func = operations[operation_symbol]
num2 = int(input("What is the second number: "))
answer = calculator_func(num1, num2)
    
print(f"{num1} {operation_symbol} {num2} = {answer}")