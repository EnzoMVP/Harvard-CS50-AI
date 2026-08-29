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
    if terminal(board):
        return None

    sum = 0
    for row in board:
        for element in row:
            if element is not None:
                sum += 1

    if sum % 2 == 0:
        return X
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    available_actions = set()
    for row in range(3):
        for column in range(3):
            if board[row][column] is None:
                available_actions.add((row, column))

    return available_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    turn_player = player(board)

    if board_copy[action[0]][action[1]] is not None:
        raise ValueError('Invalid action!')
    board_copy[action[0]][action[1]] = turn_player

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diag_a = (board[0][0], board[1][1], board[2][2])
    diag_b = (board[0][2], board[1][1], board[2][0])
    possible_win = {diag_a, diag_b}

    for i in range(3):
        row = []
        column = []
        for j in range(3):
            row.append(board[i][j])
            column.append(board[j][i])
        possible_win.add(tuple(row))
        possible_win.add(tuple(column))

    if (X, X, X) in possible_win:
        return X
    elif (O, O, O) in possible_win:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def max_value(board, alpha=float('-inf'), beta=float('inf')):
    if terminal(board):
        return utility(board)

    best_value = float('-inf')

    for action in actions(board):
        action_result = result(board, action)
        action_value = min_value(action_result, alpha, beta)

        if action_value > best_value:
            best_value = action_value

        if best_value > alpha:
            alpha = best_value

        if alpha >= beta:
            break

    return best_value

def min_value(board, alpha=float('-inf'), beta=float('inf')):
    if terminal(board):
        return utility(board)

    best_value = float('inf')

    for action in actions(board):
        action_result = result(board, action)
        action_value = max_value(action_result, alpha, beta)

        if action_value < best_value:
            best_value = action_value

        if best_value < beta:
            beta = best_value

        if beta <= alpha:
            break

    return best_value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None

    if player(board) == X:
        best_value = float('-inf')
        for action in actions(board):
            opp_best_situation = min_value(result(board, action))
            if opp_best_situation > best_value:
                best_value = opp_best_situation
                optimal_action = action
    elif player(board) == O:
        best_value = float('inf')
        for action in actions(board):
            opp_best_situation = max_value(result(board, action))
            if  opp_best_situation < best_value:
                best_value = opp_best_situation
                optimal_action = action

    return optimal_action