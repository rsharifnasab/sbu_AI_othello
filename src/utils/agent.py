from math import inf
from typing import List, Set, Dict, Tuple, Optional
from abc import ABC, abstractmethod
import numpy as np
from othello import Othello


class Agent(ABC):
    @staticmethod
    @abstractmethod
    def get_move(game: Othello, ui, turn: int):
        pass


class User(Agent):
    @staticmethod
    def get_move(game: Othello, ui, turn: int):
        ui.show_game(game)
        print(f"user, avail moves: {game.available_moves(turn)}")
        return ui.get_x_y(turn)


class Ai(Agent):

    DEPTH: int = 3

    @staticmethod
    def get_move(game: Othello, ui, turn: int):
        if not ui is None :
            ui.show_game(game)
            ui.ai_think(f"{turn} huer : {Ai.heuristic(game)}")

        (x, y), _ = Ai.minimax(game, Ai.DEPTH, ab=(-inf, +inf),
                               is_computer=True, turn=turn)

        return x, y

    # 10 < level < 50
    positional_mask = np.array([
        [100, -20, 10,  5,  5, 10, -20, 100],
        [-20, -50, -2, -2, -2, -2, -50, -20],
        [10,  -2,  -1, -1, -1, -1,  -2, -10],
        [5,   -2,  -1, -1, -1, -1,  -2,   5],
        [5,   -2,  -1, -1, -1, -1,  -2,   5],
        [10,  -2,  -1, -1, -1, -1,  -2, -10],
        [-20, -50, -2, -2, -2, -2, -50, -20],
        [100, -20, 10,  5,  5, 10, -20, 100],
    ])

    # level < 10
    mobility_mask = np.array([
        [18, 0, 0, 0, 0, 0, 0, 18],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [0,  0, 0, 0, 0, 0, 0,  0],
        [18, 0, 0, 0, 0, 0, 0, 18],
    ])

    @staticmethod
    def heuristic(game: Othello) -> int:

        # if game.steps_passed < 10:
        #    return Ai.calculate_mobility(game)
        if game.steps_passed < 50:
            return Ai.calculate_positional(game)

        return Ai.calculate_absolute(game)

    @staticmethod
    def calculate_mobility(game: Othello) -> int:
        """
        based on number of legal moves
        """
        m_player = len(game.available_moves(1))
        m_opponent = len(game.available_moves(-1))
        all_moves = m_player + m_opponent

        mult = np.sum(game.board * Ai.mobility_mask)

        if all_moves > 0:
            return mult + (m_player-m_opponent)/(m_player+m_opponent)
        else:
            return mult

    @staticmethod
    def calculate_positional(game: Othello) -> int:
        """
        based on valuable positions ( such as corners and edges)
        """
        return np.sum(game.board * Ai.positional_mask)

    @staticmethod
    def calculate_absolute(game: Othello) -> int:
        """
        based on number of pieces
        """
        return np.sum(game.board)

    @staticmethod
    def move_sorter(x : int, y : int, side : int, game: Othello) -> int:
        cl = game.clone()
        cl.play_move(x,y, side)
        return Ai.heuristic(cl)

    @staticmethod
    def minimax(game: Othello, depth: int,
                ab: Tuple[float, float],
                is_computer: bool, turn: int) -> Tuple[Tuple[int, int], float]:

        available_moves: List[Tuple[int, int]] = game.available_moves(turn)

        if depth == 0 or len(available_moves) == 0:
            return (-1, -1), Ai.heuristic(game)

        alpha, beta = ab

        best: Tuple[Tuple[int, int], float]
        if is_computer:
            best = ((-1, -1), -inf)
        else:
            best = ((-1, -1), +inf)

        # optimize tree: select relevant nodes only
        optimized_moves: List[Tuple[int, int]] = available_moves
        optimized_moves.sort(key=lambda move:
                Ai.move_sorter(move[0], move[1], turn, game))
        if depth < Ai.DEPTH - 1:  # not first minimax calls
            optimized_moves = optimized_moves[:3]

        for x, y in optimized_moves:
            # handle board copies
            game_clone = game.clone()
            game_clone.play_move(x, y, turn)
            _, score = Ai.minimax(game_clone, depth-1, (alpha, beta),
                                  not is_computer, turn * -1)

            # maximizer
            if is_computer and (score >= best[1]):
                best = ((x, y), score)
                alpha = max(alpha, best[1])

            # minimizer
            if (not is_computer) and (score <= best[1]):
                best = ((x, y), score)
                beta = min(beta, best[1])

            # prune
            if beta <= alpha:
                break

        return best
