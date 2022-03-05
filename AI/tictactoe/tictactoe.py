"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    count = sum([count+1 for row in board for cell in row if cell != EMPTY])

    if count%2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board = copy.deepcopy(board)
    temp_board[action[0]][action[1]] = player(board)
    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check the 2 diagonals for winner
    diagonal = {board[i][i] for i in range(3)}
    if len(diagonal) == 1 and EMPTY not in diagonal:
        return X if X in diagonal else O
    diagonal = {board[2-i][i] for i in range(2,-1,-1)}
    if len(diagonal) == 1 and EMPTY not in diagonal:
        return X if X in diagonal else O

    # check rows for winner
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # check cols for winner
    for i in range(3):
        col = [row[i] for row in board]
        if all(cell == X for cell in col):
            return X
        elif all(cell == O for cell in col):
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # found winner
    if winner(board) is not None:
        return True
    # not fully filled
    if EMPTY in {row[i] for row in board for i in range(3)}:
        return False
    # filled == tie
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    xam=-math.inf
    nim=math.inf

    def MaxV(board,xam,nim):
        if terminal(board):
            return utility(board), None
        value = -math.inf
        move = None
        for action in actions(board):
            temp = MinV(result(board,action),xam,nim)[0]
            if temp > value:
                value = temp
                move = action
            xam = max(xam,temp)
            if xam > nim:
                break
        return value, move

    def MinV(board,xam,nim):
        if terminal(board):
            return utility(board), None
        value = math.inf
        move = None
        for action in actions(board):
            temp = MaxV(result(board,action),xam,nim)[0]
            if temp < value:
                value = temp
                move = action
            nim=min(nim,temp)
            if nim < xam:
                break
        return value, move

    if player(board) == X:
        return MaxV(board,xam,nim)[1]
    else:
        return MinV(board,xam,nim)[1]