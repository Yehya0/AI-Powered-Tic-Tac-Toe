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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    # Deep copy the board to create a new board state
    new_board = [row[:] for row in board]
    
    # Determine the current player
    current_player = player(board)
    
    # Update the new board with the current player's move
    (i, j) = action
    new_board[i][j] = current_player

    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and columns for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[2][0]

    # No winner found
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check for any EMPTY cell, if found game is not over
    for row in board:
        if EMPTY in row:
            return False

    # No EMPTY cells and no winner means the game ended in a tie
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

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    best_move = None
    for action in actions(board):
        v2, _ = min_value(result(board, action))
        if v2 > v:
            v, best_move = v2, action
    return v, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    best_move = None
    for action in actions(board):
        v2, _ = max_value(result(board, action))
        if v2 < v:
            v, best_move = v2, action
    return v, best_move
