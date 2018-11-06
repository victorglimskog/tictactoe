example_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
board = [ ' ' for num in range(0,10) ]
active_player = 0

def print_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')

# Intro
print('This is a tic tac toe game for 2 players. Input a move by pressing a number corresponding to a space')
print_board(example_board)

# Receive the players preferred symbol and uppercase it
# Also validate that the input is either X or O
players = tuple(input('First player, do you want to be X or O?\n').upper())

while players[0] not in ('X', 'O'):
    players = tuple(input('You must choose either X or O. Please try again!\n').upper())

if players[0] == 'X':
    players += ('O',)
else:
    players += ('X',)

# Prompt players to start the game
input(f'player one is {players[0]}. Press any key to play!')
print_board(board)

def next_active_player(active_player):
    if active_player == 1:
        next_player = 0
    else:
        next_player = 1

    return next_player

def make_move(index):
    board[index] = players[active_player]

def get_next_move():
    while True:
        try:
            next_move_index = int(input(f'Player {players[active_player]}, What is your next move? \n'))
            if board[next_move_index] != ' ':
                print('That spot is already taken')
                continue
        except ValueError:
            print('You must enter an integer between 1 and 9. Try again!')
            continue
        else:
            return next_move_index

def check_draw():
    empty_spaces = list(filter(lambda space: space == ' ', board))
    if len(empty_spaces) <= 1:
        return True
    else:
        return False

def check_win(player):
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


def check_game_status():

    if check_win('X'):
        print('player X won')
        return False
    elif check_win('O'):
        print('player O won')
        return False
    elif check_draw():
        print('game ended in a draw')
        return False
    else:
        return True

# Game loop
while check_game_status():
    next_move_index = get_next_move()
    make_move(next_move_index)
    print_board(board)
    active_player = next_active_player(active_player)