import os

os.system('cls' if os.name == 'nt' else 'clear')

keep_running = True

while keep_running:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == 'yes':
        keep_running = True
        os.system('cls' if os.name == 'nt' else 'clear')
    elif answer == 'no':
        keep_running = False
        #print(f"The winner is {winner} with a bid of ${winning_bid}")
