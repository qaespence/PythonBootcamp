# <summary>
# Udemy course - Complete Python Bootcamp
# Section 7: Milestone Project - 1
# TicTacToe game
# </summary>

player_pieces = []

def display_board(display_board):
    print("   |   |   ")
    print(" " + display_board[7] + " | " + display_board[8] + " | " + display_board[9])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + display_board[4] + " | " + display_board[5] + " | " + display_board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + display_board[1] + " | " + display_board[2] + " | " + display_board[3])
    print("   |   |   ")
    pass

def player_input():
    pieces = ['x','o']
    while True:
        piece = input("Player 1, please pick a marker 'X' or 'O':  ").lower()
        if piece[0] not in pieces:
            print("I don't understand {0}.".format(piece[0]))
            continue
        else:
            if piece[0] == 'o':
                return ['O', 'X']
            else:
                return ['X', 'O']

def place_marker(board, marker, position):
    pieces = ['X','O']
    if board[position] not in pieces:
        board[position] = marker
    return board

def not_replay():
    choice = input("Play again?").lower()
    if choice == 'y' or choice == 'yes':
        return False
    return True

def choose_position(board, player):
    pieces = ['X','O']
    while True:
        choice = int(input("Player {0}, which position (see num pad)? ".format(player)))
        if choice not in range(1,10):
            print("Oops! That isn't a board position!")
            continue
        if board[choice] in pieces:
            print("Oops! That position is already taken!")
            continue
        board = place_marker(board, player, choice)
        return board

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False;
    return True

def check_for_winner(board, marker):
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
    game_on = True
    game_board = [' ']*10
    player_pieces = player_input()

    while game_on:
        # Player 1 turn
        display_board(game_board)
        choose_position(game_board, player_pieces[0])
        game_on = not check_for_winner(game_board, player_pieces[0]);
        if not game_on:
            break
        # Player 2 turn
        display_board(game_board)
        choose_position(game_board, player_pieces[1])
        game_on = not check_for_winner(game_board, player_pieces[1]);

    if not_replay():
        break
