from art import logo, vs
from game_data import data
import random
import os


def get_options():
    """Initializes picks for the game to function"""
    option = random.choice(data)
    return option


def name(option):
    """Gets the name key of the dictionary"""
    return option["name"]


def description(option):
    """Gets the description key of the dictionary"""
    return option["description"]

    
def country(option):
    """Gets the country key of the dictionary"""
    return option["country"]


def compare_followers(option_a, option_b):
    """Checks which one has more followers"""
    if option_a["follower_count"] > option_b["follower_count"]:
        return option_a["follower_count"]
    else:
        return option_b["follower_count"]


score = 0  # Global variable so that we don't lose our score
game_over = False  # Also needs to be global so we can see if the game is over
option_b = get_options()

while not game_over:
    print(logo)
    option_a = option_b
    print(f"Compare A: {name(option_a)}, a {description(option_a)}, from {country(option_a)}.")
    # Debugging print:
    # print(option_a["follower_count"])
    print(vs)
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)
    print(f"Against B: {name(option_b)}, a {description(option_b)}, from {country(option_b)}.")
    # Debugging print:
    # print(option_b["follower_count"])
    more_followers = compare_followers(option_a, option_b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        if option_a["follower_count"] == more_followers:
            score += 1
            os.system("cls" if os.name == "nt" else "clear")
            print(f"You're right! Current score: {score}")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
          
    elif guess == "b":
        if option_b["follower_count"] == more_followers:
            score += 1
            os.system("cls" if os.name == "nt" else "clear")
            print(f"You're right! Current score: {score}")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

