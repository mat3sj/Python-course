def create_board(size: int) -> list:
    result = []
    n = 1
    for i in range(size):
        line =[]
        for j in range(size):
            line.append(' ')
            n += 1
        result.append(line)
    return result

def print_board(board: list) -> print:
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

def win_game(board: list, sym: str) -> bool:
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

    left_dia = []
    right_dia = []
    for idx in range(len(board)):
        left_dia.append(board[idx][len(board)-idx-1])
        right_dia.append(board[idx][idx])
    if opponent not in left_dia and ' ' not in left_dia:
        return True
    if opponent not in right_dia and ' ' not in right_dia:
        return True

def move(board: list, sym: str, my_move: int) -> list:
    possition = 1
    for idx, line in enumerate(board):
        for jdx, _ in enumerate(line):
            if possition == my_move:
                board[idx][jdx] = sym
            possition += 1
    return board

def tic_tac_toe(size: int):
    board = create_board(size)
    possible_moves = list(range(1,size**2+1))
    print_board(board)
    switch = ['x','o']
    counter = 1
    while True:
        sym = switch[counter%2]
        if sym == 'o':
            print('Player 1 is on the move')
            my_move = int(input('Your move: '))
        else:
            print('Player 2 is on the move')
            my_move = int(input('Your move: '))
        if my_move not in possible_moves:
            print('Your move is not possible to play')
            continue
        possible_moves.remove(my_move)
        board = move(board,sym,my_move)
        print_board(board)
        counter += 1
        if win_game(board,sym):
            print (f'{sym} has won the game')
            break
    print ('Thank you for playing :-)')
    return
tic_tac_toe(5)
    