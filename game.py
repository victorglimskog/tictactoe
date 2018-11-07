def print_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')

def intro():
    print('This is a tic tac toe game for 2 players. Input a move by pressing a number corresponding to a space')
    example_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(example_board)

def player_symbols():
    # Receive the players preferred symbol and uppercase it
    # Also validate that the input is either X or O
    # players = tuple(input('First player, do you want to be X or O?\n').upper())
    while True:
        try:
            players = tuple(input('First player, do you want to be X or O?\n').upper())
            if not players or players[0] not in ('X', 'O'):
                print('You must choose either X or O. Please try again!')
                continue

            if players[0] == 'X':
                players += ('O',)
            else:
                players += ('X',)
        except ValueError:
            print('You must choose either X or O. Please try again!')
            continue
        else:
            return players

# Intro
def init_game():
    intro()
    players = player_symbols()
    # Prompt players to start the game
    input(f'player one is {players[0]}. Press any key to play!')
    game(players)

def next_active_player(active_player):
    if active_player == 1:
        next_player = 0
    else:
        next_player = 1

    return next_player

def make_move(index, board, player):
    board[index] = player

def get_next_move(player, board):
    while True:
        try:
            next_move_index = int(input(f'Player {player}, What is your next move? \n'))
            if board[next_move_index] != ' ':
                print('That spot is already taken')
                continue
        except ValueError:
            print('You must enter an integer between 1 and 9. Try again!')
            continue
        else:
            return next_move_index

def check_draw(board):
    empty_spaces = list(filter(lambda space: space == ' ', board))
    if len(empty_spaces) <= 1:
        return True
    else:
        return False

def check_win(player, board):
    win = False
    winning_sequences = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,5,8),
        (3,6,9),
        (1,5,9),
        (3,5,7)
    ]

    for sequence in winning_sequences:
        # print(f'{board[sequence[0]]}{board[sequence[1]]}{board[sequence[2]]}' + f'{player*3}')
        if f'{board[sequence[0]]}{board[sequence[1]]}{board[sequence[2]]}' == f'{player*3}':
            win = True

    return win


def check_game_status(board):

    if check_win('X', board):
        print('player X won')
        return False
    elif check_win('O', board):
        print('player O won')
        return False
    elif check_draw(board):
        print('game ended in a draw')
        return False
    else:
        return True

# Game loop
def game(players):
    board = [ ' ' for num in range(0,10) ]
    active_player = 0

    print_board(board)

    while check_game_status(board):
        next_move_index = get_next_move(players[active_player], board)
        make_move(next_move_index, board, players[active_player])
        print_board(board)
        active_player = next_active_player(active_player)

    play_again = input('Press X to exit game, press any key to play again.').upper()
    if play_again != 'X':
        init_game()

init_game()