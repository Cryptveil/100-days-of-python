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
        hand.append(1)
    return sum(hand)


def compare (player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You lose 😤"
    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose 😤"
    elif player_score == 0:
        return "You win 😃"
    elif computer_score > 21:
        return "You win 😃"
    elif player_score > 21:
        return "You lose 😤"
    elif player_score > computer_score:
        return "You win 😃"
    elif player_score < computer_score:
        return "You lose 😤"


def play_game():
    print(logo)
    player_hand = []
    computer_hand = []
    game_is_running = True

    # Draws two cards for both the player and the computer
    for i in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while game_is_running:
            # Gets the player score (sum of all the cards on hand)
            player_score = calculate_score(player_hand)
            computer_score = calculate_score(computer_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
            print(f"Computer's first card: {computer_hand[0]}")
            # Checks if the game should be over

            if player_score == 0 or computer_score == 0 or player_score > 21:
                game_is_running = False
            else:
            # Loop to see if the player will continue drawing cards
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "y":
                    # Draws another card
                    player_hand.append(deal_card())
                else:
                    game_is_running = False

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls" if os.name == "nt" else "clear")
    play_game()
