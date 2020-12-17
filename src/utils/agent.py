import numpy as np
from math import inf


class User():
    @staticmethod
    def get_move(game, ui, turn):
        ui.show_game(game)
        print(f"user, avail moves: {game.available_moves(turn)}")
        return ui.get_x_y(turn)


class Ai():
    @staticmethod
    def get_move(game, ui, turn):
        ui.show_game(game)
        ui.ai_think(turn)

        depth = 9
        (x, y), _ = Ai.minimax(game, depth, alpha=-inf, beta=+inf,
                               is_computer=True, turn=turn)

        return x, y

    @staticmethod
    def heuristic(board, steps_passed):
	
        if board.steps_passed < 10:
            return calculate_mobility(board)
        elif board.steps_passed < 50:
            return calculate_positional(board)
        else:
            return calculate_absolute(board)



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


    @staticmethod
    def minimax(game, depth, alpha, beta, is_computer, turn):
        if depth == 0 or game.game_over():
            return (-1, -1), Ai.heuristic(game)

        if is_computer:
            best = [(-1, -1), -inf]
        else:
            best = [(-1, -1), +inf]


        for x, y in game.available_moves(turn):
            # handle board copies
            game_clone = game.clone()
            game_clone.play_move(x, y, turn)
            _, score = Ai.minimax(game_clone, depth-1, alpha,
                                  beta, not is_computer, turn * -1)

            # maximizer
            if is_computer and (score >= best[1]):
                best = [(x, y), score]
                alpha = max(alpha, best[1])

            # minimizer
            if (not is_computer) and (score < best[1]):
                best = [(x, y), score]
                beta = min(beta, best[1])

            # prune?
            if beta <= alpha:
                break

        return best
