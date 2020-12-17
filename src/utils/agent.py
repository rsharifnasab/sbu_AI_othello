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
        if steps_passed < 10:
            return calculate_mobility(board)
        elif steps_passed < 50:
            return calculate_positional(board)
        else:
            return calculate_absolute(board)

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


    @staticmethod
    def calculate_positional(board):
        """
        based on valuable positions ( such as corners and edges)
        """
        mask = np.array([
            [100, -20, 10,  5,  5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10,  -2,  -1, -1, -1, -1,  -2, -10],
            [5,   -2,  -1, -1, -1, -1,  -2,   5],
            [5,   -2,  -1, -1, -1, -1,  -2,   5],
            [10,  -2,  -1, -1, -1, -1,  -2, -10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10,  5,  5, 10, -20, 100],
            ])
        return np.multiply(board, mask)
    
    @staticmethod
    def calculate_mobility(board):
        """
        based on number of legal moves
        """
        mask = np.array([
            [2, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 2],
            ])
        m_player = board.available_moves(1)
        m_opponent = board.available_moves(-1)
        return 10*np.multiply(board, mask) + (m_player-m_opponent)/(m_player+m_opponent)

    @staticmethod
    def calculate_absolute(board):
        """
        based on number of pieces
        """
        return np.sum(board)