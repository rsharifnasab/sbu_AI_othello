import numpy as np
from math import inf


class User():
    @staticmethod
    def get_move(game, ui, turn):
        ui.show_game(game)
        return ui.get_x_y(turn)


class Ai():
    @staticmethod
    def get_move(game, ui, turn, steps_passed):
        ui.show_game(game)
        ui.ai_think(turn)

        depth = 3
        (x, y), _ = Ai.minimax(game, depth, alpha=-inf, beta=+inf,
                               is_computer=True, turn=turn, steps_passed=steps_passed)

        return x, y

    @staticmethod
    def heuristic(board, steps_passed):
        steps_passed += 1
        return np.sum(board)

    @staticmethod
    def minimax(game, depth, alpha, beta, is_computer, turn, steps_passed):
        if depth == 0 or game.game_over():
            return (-1, -1), heuristic(game.board, steps_passed)

        if is_computer:
            best = [(-1, -1), -inf]
        else:
            best = [(-1, -1), +inf]


        for x,y in game.available_moves(turn):
            pass

