############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo
import os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
player_hand = []
computer_hand = []
state = ["You win 😃", "You lose 😤"]
player_score = 0
computer_score = 0
game_is_running = True

while game_is_running:
    more_cards = True
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "y":
        computer_hand.append(random.choice(deck))
        for i in range(2):
            player_hand.append(random.choice(deck))
        player_score = sum(player_hand)
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        while more_cards:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                print(f"Your cards: , current score: ")
                print(f"Computer's first card: ")
            else:
                print(f"Your final hand: , final score: ")
                print(f"Computer's final hand: , final score: ")
                more_cards = False
                player_hand = []
                computer_hand = []

    else:
        game_is_running = False
