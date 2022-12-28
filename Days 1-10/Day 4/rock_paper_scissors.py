import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ['Rock', 'Paper', 'Scissors']

computer = random.choice(choices)

player = None 

while player not in choices:

    player = input("Rock, paper or scissors? ").capitalize()

    if player == computer:
        print(f"You chose: {player}")
        if player == "Rock":
            print(rock)
        elif player == "Scissors":
            print(scissors)
        elif player == "Paper":
            print(paper)
        print(f"The computer chose: {computer}")
        if computer == "Rock":
            print(rock)
        elif computer == "Scissors":
            print(scissors)
        elif computer == "Paper":
            print(paper)    
        print("Tie!")
    elif player == 'Rock':
        if computer == 'Scissors':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You won!")
        if computer == 'Paper':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You lose!")

    elif player == 'Paper':
        if computer == 'Rock':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You won!")
        if computer == 'Scissors':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You lose!")
 
    elif player == 'Scissors':
        if computer == 'Paper':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You won!")
        if computer == 'Rock':
            print(f"You chose: {player}")
            if player == "Rock":
                print(rock)
            elif player == "Scissors":
                print(scissors)
            elif player == "Paper":
                print(paper)       
            print(f"The computer chose: {computer}")
            if computer == "Rock":
                print(rock)
            elif computer == "Scissors":
                print(scissors)
            elif computer == "Paper":
                print(paper)       
            print("You lose!")

