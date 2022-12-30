from art import logo
import random
import os


def chosen_number():
    """This function just chooses a random number between 1 and 100"""
    return random.choice(range(1,101))


def chosen_difficulty():
    """This function chooses the difficulty, easy gets 10 tries and hard gets 5"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        health = 10
    elif difficulty == "hard":
        health = 5
    else:
        print("You had to type 'easy' or 'hard'. Now you lost. Look at you.")
        health = 0
    return health


def decrease_health():
    """Decreases health by one point"""
    return health - 1


def check_guess(guess, answer):
    """Checks the guess"""
    if guess == answer:
        print(f"Hey you got it, the answer was {answer}. Are you cheating?")
        return True
    elif guess > answer:
        print("Too high!")
        return False
    elif guess < answer:
        print("Too low!")
        return False


def play_game():
    """Starts the game!"""
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("Try to guess a number between 1 and 100.")
    global health  # Could also declare a few global variables for the health
                   # and use them outside here
    health = chosen_difficulty()  # Will start the health variable based on the
                                  # chosen difficulty 
    answer = chosen_number()  # Initializes the chosen number
    #print(f"The answer is: {answer}")  # Debugging tool

    while health > 0:
        print(f"You have {health} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check = check_guess(guess, answer)
        if check:
            health = 0
        else:
            health = decrease_health()
            if health > 0:
                print("Guess again.")
            else: 
                print("You lose loooooool")


play_game()

while input("Do you wanna play again? Type 'y' or 'n': ") == "y":
    play_game()
