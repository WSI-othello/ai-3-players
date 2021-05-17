from copy import deepcopy

from board import Board, EMPTY


def minimax(board: Board, depth: int, maximizing_player: int, current_player: int, num_players: int, turns_passed: int, heuristic):
    # max depth reached or game ended
    if depth == 0 or turns_passed == num_players:
        return heuristic(board, current_player)

    max_eval = None
    valid_moves = board.valid_moves(current_player)
    next_player = (current_player + 1) % num_players

    # handle case when player has no valid moves (skip him, but continue minimax)
    if not valid_moves:
        return minimax(deepcopy(board), depth - 1, maximizing_player, next_player, num_players, turns_passed + 1, heuristic)

    for move_row, move_col in valid_moves:
        board.place(move_row, move_col, current_player)
        evaluation = minimax(board, depth - 1, maximizing_player, next_player, num_players, 0, heuristic)
        board.board[move_row][move_col] = EMPTY
        f = max if current_player == maximizing_player else min
        max_eval = evaluation if max_eval is None else f(max_eval, evaluation)

    return max_eval
