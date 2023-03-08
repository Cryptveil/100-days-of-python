import os
import random

IS_GAME_OVER = False

board = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " ",
        }

winning_combinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
    [1, 5, 9], [7, 5, 3]              # diagonal
]


def guide():
    clear_screen()
    print("Positions are as follow:")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def available_moves(board):
    return [x for x in board.keys() if board[x] == " "]


def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def update_board(letter, position):
    global IS_GAME_OVER
    if board[position] == " ":
        board[position] = letter
        print_board(board)
        if check_for_winner():
            if letter == "X":
                print("Computer wins!")
                IS_GAME_OVER = True
            else:
                print("Damn you actually won against that thing, good job!")
                IS_GAME_OVER = True
        elif check_draw():
            print("Draw!")
            IS_GAME_OVER = True
    else:
        clear_screen()
        guide()
        print_board(board)
        print("You can't choose this position dummy!")
        new_position = int(input("Choose a valid position: "))
        update_board(letter, new_position)


def check_for_winner():
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == \
                board[combination[2]] != " ":
            return True
    return False


def check_draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def computer():
    if len(available_moves(board)) == 9:
        position = random.randint(1, 9)
        update_board("X", position)
    else:
        move = random.choice(available_moves(board))
        update_board("X", move)


def minimax(board, player):
    pass


guide()
computer()

while not IS_GAME_OVER:
    try:
        position = int(input("Choose the position to update the board"
                             " (1-9 to update, 0 to quit): "))
    except ValueError:
        print("Numbers only, please.")
    else:
        if position == 0:
            exit()
        clear_screen()
        try:
            guide()
            update_board("O", position)
            clear_screen()
        except KeyError:
            print("That position doesn't even exist. Are you trolling?")
        else:
            computer()
