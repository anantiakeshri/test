#This game is about encoding snd decoding message using shift amount

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from Cipher_art import logo
print(logo)

def ceaser(plain_text, shift_amount, cipher_direction):
    start_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            start_text += alphabet[new_position]
        else: 
            start_text += char
    print(f"The {cipher_direction}d text is {start_text}.")
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(plain_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Do you want to continue? Type 'yes' to continue and 'no' to stop.\n").lower()
    if result == "no":
        should_continue = False
        print("Bye, have a nice day!")
        
#This code is written by Anantia Keshri