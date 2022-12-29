import random
from art import logo
import os


def deal_card():
    """ Returns a random card when called """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    card = random.choice(deck)
    return card


def calculate_score(hand):
    """ Calculates the score and returns it """
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        cards.append(1)
    return sum(hand)


player_hand = []
computer_hand = []
state = ["You win 😃", "You lose 😤"]
game_is_running = True
game_over = False

while game_is_running:
    more_cards = True
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "y":
        # Draws two cards for both the player and the computer
        for i in range(2):
            player_hand.append(deal_card())
            computer_hand.append(deal_card())
        # Gets the player score (sum of all the cards on hand)
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(player_hand)
        # Checks if the game should be over
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True

        # Clears the terminal for better user experience
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        # Loop to see if the player will continue drawing cards
        while more_cards:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                # Draws another card
                player_hand.append(deal_card())
                player_score = calculate_score(player_hand)
                if player_score > 21:
                    pass
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's first card: {computer_hand[0]}")
            else:
                computer_score = calculate_score(computer_hand)
                print(f"Your final hand: {player_hand}, final score: {player_score}")
                print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
                more_cards = False
                player_hand = []
                computer_hand = []

    else:
        game_is_running = False
