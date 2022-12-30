from art import logo
import random


def chosen_number():
    return random.choice(range(1,101))


def chosen_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        health = 10
    elif difficulty == "hard":
        health = 5
    else:
        print("You had to type 'easy' or 'hard'. Now you lost. Look at you.")
        health = 0
    return health


def is_game_over(health):
    if health == 0:
        return True
    return False


def decrease_health():
    return health - 1


print(logo)
print("Welcome to the Number Guessing Game!")
print("Try to guess a number between 1 and 100.")

health = chosen_difficulty()
print(health)
decrease_health()
print(health)




