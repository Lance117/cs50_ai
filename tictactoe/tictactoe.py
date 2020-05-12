"""
Tic Tac Toe Player
"""

import math

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

def count(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                count += 1
    return count

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return O if count(board) % 2 else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j]:
                res.add((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    next_board = [row[:] for row in board]
    next_board[i][j] = player(board)
    return next_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
    ]
    for line in lines:
        if all([e == line[0] for e in line]):
            return line[0]
    return None

def draw(board):
    return not winner(board) and count(board) == 9

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) or draw(board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == 0:
        return -1
    return 0

def max_player(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_player(result(board, action)))
    return v

def min_player(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_player(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    for action in actions(board):
        return action