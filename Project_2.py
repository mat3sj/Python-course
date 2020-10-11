import random

def create_board(size: int) -> list:
    result = [[' ' for _ in range(size)] for i in range(size)]
    return result

def print_board(board: list) -> print: # Prints given state of the board nicely
    template_lst = ['']
    size = len(board)
    for _ in range(size):
        template_lst.append('{:^3}')
    template_lst.append('')
    template = '|'.join(template_lst)
    print('-'*size*4)
    for line in board:
        print(template.format(*line))
        print('-'*size*4)

def is_won(board: list, sym: str) -> bool: # Testing if the game is won - not very happy with this solution
    if sym == 'x':
        opponent = 'o'
    else:
        opponent = 'x'

    for idx,line in enumerate(board):
        if opponent not in line and ' ' not in line:
            return True
        column = []
        for jdx, _ in enumerate(line):
            column.append(board[jdx][idx])
        if opponent not in column and ' ' not in column:
            return True

    left_dia = [board[idx][len(board)-idx-1] for idx in range(len(board))]
    right_dia = [board[idx][idx] for idx in range(len(board))]

    if opponent not in left_dia and ' ' not in left_dia:
        return True
    if opponent not in right_dia and ' ' not in right_dia:
        return True

def move(board: list, sym: str, my_move: int) -> list: # Processing single move by adding symbol to given cell
    size = len(board)
    x = (my_move - 1) // size
    y = (my_move -1) % size 
    board[x][y] = sym
    return board

def get_lines(board: list, move: int) -> list: # Returns all relevant lines (column, row and diagonals(if present))
    x = (move-1) // len(board)
    y = (move-1) % len(board)
    line = []
    column = []
    left_dia = []
    right_dia = []
    for idx, _ in enumerate(board):
        line.append(board[x][idx])
        column.append(board[idx][y])
        if x == y:
            left_dia.append(board[idx][idx])
        if x == (len(board)-y-1):
            right_dia.append(board[idx][len(board)-idx-1])
    return line, column, left_dia, right_dia

def evaluate(board: list, move: int, sym: str) -> int: #evaluate given move in current situation
    values = []
    if sym == 'x':
        me = 0
    else:
        me = 1
    
    players = ['x','o']
    result = 0
    bot = 0
    all_lines = list(get_lines(board, move))
    for line in all_lines:
        opp = 0
        mine = 0
        if line:
            for cell in line:
                if cell == players[me]:
                    mine += 1
                elif cell == players[1-me]:
                    opp += 1
            if mine == 0:
                if opp != 0:    
                    values.append(opp+1)
                else:
                    values.append(1)
            else:
                if opp == 0:
                    values.append(mine+1)
    for num in values:
        result += 2**num
    return result

def best_move(board: list, sym: str) -> int: #looking for a best possible move. If there are more of them, it choose it randomly
    move = 1
    current = 0
    best = 0
    set_of_moves = []
    for line in board:
        for cell in line:
            if cell ==' ':
                current = evaluate(board, move, sym)
                if current == best:
                    set_of_moves.append(move)
                elif current > best:
                    set_of_moves = []
                    set_of_moves.append(move)
                    best = current
            move += 1
    result = random.choice(set_of_moves)
    return result

def is_end(board: list) -> bool: #testing if all cells are full
    for line in board:
        for cell in line:
            if cell == ' ':
                return False
    return True

def is_possible(moves: list, move) -> bool:
    if move in moves:
        moves.remove(move)
        return True
    else:
        return False

def tic_tac_toe(size: int): # The main program
    board = create_board(size)
    possible_moves = list(range(1,size**2+1))
    print_board(board)
    switch = ['x','o']
    counter = 1
    while True:
        sym = switch[counter%2]
        if sym == 'o':
            print('Player 1 is on the move')
            #my_move = best_move(board, sym)
            my_move = int(input('Your move: '))
        else:
            print('Player 2 is on the move')
            #my_move = best_move(board, sym)
            my_move = int(input('Your move: '))
        if not is_possible(possible_moves, my_move):
            print('Your move is not possible to play')
            continue

        board = move(board,sym,my_move)
        print_board(board)
        counter += 1
        if is_won(board,sym):
            print (f'{sym} has won the game')
            break
        if is_end(board):
            print('This is a tie!')
            break
    print ('Thank you for playing :-)')
    return

tic_tac_toe(3)