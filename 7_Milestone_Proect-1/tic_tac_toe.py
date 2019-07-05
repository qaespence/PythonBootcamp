# <summary>
# Udemy course - Complete Python Bootcamp
# Section 7: Milestone Project - 1
# TicTacToe game
# </summary>

PLAYERPIECES = []

def display_board(board):
    """ Display the game board on the console """
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   \n")

def player_input():
    """ Determine if Player 1 is X or O """
    pieces = ['x', 'o']
    while True:
        piece = input("Player 1, please pick a marker 'X' or 'O':  ").lower()
        if piece[0] not in pieces:
            print("I don't understand {0}.".format(piece[0]))
            continue
        else:
            if piece[0] == 'o':
                return ['O', 'X']
            return ['X', 'O']

def place_marker(board, marker, position):
    """ Place a player marker on the game board """
    pieces = ['X', 'O']
    if board[position] not in pieces:
        board[position] = marker
    return board

def not_replay():
    """ Ask if the player wants to play another game """
    choice = input("Play again?").lower()
    if choice in ('y', 'yes'):
        return False
    return True

def choose_position(board, player):
    """ Ask where the player wishes to play their piece at """
    pieces = ['X', 'O']
    while True:
        choice = int(input("Player {0}, which position (see num pad)? ".format(player)))
        if choice not in range(1, 10):
            print("Oops! That isn't a board position!")
            continue
        if board[choice] in pieces:
            print("Oops! That position is already taken!")
            continue
        board = place_marker(board, player, choice)
        return board

def space_check(board, position):
    """ Check the board if the position is empty """
    return board[position] == ' '

def full_board_check(board):
    """ Check if the board is full for a tie game """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def check_for_winner(board, marker):
    """ Test for a winning player or tie """
    if (board[1] == board[2] == board[3] == marker) or \
        (board[4] == board[5] == board[6] == marker) or \
        (board[7] == board[8] == board[9] == marker) or \
        (board[7] == board[4] == board[1] == marker) or \
        (board[8] == board[5] == board[2] == marker) or \
        (board[9] == board[6] == board[3] == marker) or \
        (board[7] == board[5] == board[2] == marker) or \
        (board[9] == board[5] == board[1] == marker):
        print("YAY! Player {0} wins!".format(marker))
        display_board(board)
        return True
    if full_board_check(board):
        print("Oh well, it's a tie")
        display_board(board)
        return True
    return False

# Main game loop
while True:
    print("Welcome to Tic Tac Toe!")

    # Set up the game
    GAMEON = True
    GAMEBOARD = [' ']*10
    PLAYERPIECES = player_input()

    while GAMEON:
        # Player 1 turn
        display_board(GAMEBOARD)
        choose_position(GAMEBOARD, PLAYERPIECES[0])
        GAMEON = not check_for_winner(GAMEBOARD, PLAYERPIECES[0])
        if not GAMEON:
            break
        # Player 2 turn
        display_board(GAMEBOARD)
        choose_position(GAMEBOARD, PLAYERPIECES[1])
        GAMEON = not check_for_winner(GAMEBOARD, PLAYERPIECES[1])

    if not_replay():
        break
