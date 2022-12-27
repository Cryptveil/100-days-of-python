import os
from art import logo

# Clears the chat
os.system('cls' if os.name == 'nt' else 'clear')

bidder_dictionary = {}
keep_running = True
winner_name = max(bidder_dictionary, key=bidder_dictionary.get)
winning_bid = max(bidder_dictionary.values())

print(logo)
print("Welcome to the secret auction program.")

while keep_running:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidder_dictionary[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if answer == 'yes':
        keep_running = True
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif answer == 'no':
        keep_running = False
        print(f"The winner is {winner_name} with a bid of ${winning_bid}")

    else:
        keep_running = False
        print("Your options were 'yes' or 'no'!")
