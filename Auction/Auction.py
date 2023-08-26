#It is a Blind Auction biding program.

import os

from Auction_logo import logo
print(logo)

auction = {}
bid_completed = False

def auction_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and bidding amount is ${highest_bid}.")
    
while not bid_completed: 
    name = input("What is your name?: ")
    bid = int(input("How much do you want to bid? $"))
    auction[name] = bid
    request = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if request == "no":
        bid_completed = True
        auction_bid(auction)
    elif request == "yes":
        os.system('cls')
        
#This code is written by Anantia Keshri.