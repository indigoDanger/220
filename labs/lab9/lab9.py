"""
Name: <Indigo Dockery>
<lab8>.py

Problem: <This program develops a Python program that uses the built-in
list functions and boolean logic, and develops while control structures.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def build_board():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return num_list


def fill_spot(board: list, position: int, shape):
    board[position - 1] = shape.strip().lower()


def is_legal(board: list, position: int):
    occupied = board[position - 1]
    if not position == occupied:
        return True
    else:
        return False


def game_is_won(board: list):
    winner1 = board[0] == board[1] == board[2]
    winner2 = board[3] == board[4] == board[5]
    winner3 = board[6] == board[7] == board[8]
    winner4 = board[0] == board[3] == board[6]
    winner5 = board[1] == board[4] == board[7]
    winner6 = board[2] == board[5] == board[8]
    winner7 = board[0] == board[4] == board[8]
    winner8 = board[2] == board[4] == board[6]
    if winner1:
        return True
    elif winner2:
        return True
    elif winner3:
        return True
    elif winner4:
        return True
    elif winner5:
        return True
    elif winner6:
        return True
    elif winner7:
        return True
    elif winner8:
        return True
    else:
        return False


def game_over(board: list):
    if game_is_won(board):
        return True
    for i in board:
        full = str(i)
        if full.isnumeric():
            return False
    return True


def get_winner(board: list):
    winner1 = board[0] == board[1] == board[2]
    winner2 = board[3] == board[4] == board[5]
    winner3 = board[6] == board[7] == board[8]
    winner4 = board[0] == board[3] == board[6]
    winner5 = board[1] == board[4] == board[7]
    winner6 = board[2] == board[5] == board[8]
    winner7 = board[0] == board[4] == board[8]
    winner8 = board[2] == board[4] == board[6]
    if winner1:
        return board[0]
    elif winner2:
        return board[3]
    elif winner3:
        return board[6]
    elif winner4:
        return board[0]
    elif winner5:
        return board[1]
    elif winner6:
        return board[2]
    elif winner7:
        return board[0]
    elif winner8:
        return board[2]
    else:
        return None


def play(board):
    while play(board):
        player_one = 0
        player_two = 1

        while not game_over(board):
            if player_one % 2 == 0:
                player_one = player_one + 2
                shape = "x"
                user = eval(input("x's, choose a position: "))
            elif player_two % 2 == 1:
                player_two = player_two + 2
                shape = "o"
                user = eval(input("o's, choose a position: "))
            build_board()
            fill_spot(board, user, shape)
            is_legal(board, user)
            game_is_won(board)
            game_over(board)
            get_winner(board)
    start_over = input("play again? ").lower()
    if start_over == "y":
        print_board(board)
        build_board()
        position = 0
        fill_spot(board, position, shape)
        is_legal(board, position)
        game_is_won(board)
        game_over(board)
        get_winner(board)
    play(board)

