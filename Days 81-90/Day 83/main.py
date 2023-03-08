import os

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
        if check_draw():
            print("Draw!")
            IS_GAME_OVER = True
    else:
        print("You can't choose this position dummy!")


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


guide()
print_board(board)

while not IS_GAME_OVER:
    position = int(input("Choose the position to update the board: "))
    clear_screen()
    try:
        guide()
        update_board("O", position)
    except KeyError:
        print("That position doesn't even exist. Are you trolling?")
