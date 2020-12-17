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

        depth = 5
        (x, y), _ = Ai.minimax(game, depth, alpha=-inf, beta=+inf,
                               is_computer=True, turn=turn)

        return x, y

    @staticmethod
    def heuristic(game):
        # game.steps_passed
        return np.sum(game.board)

    @staticmethod
    def minimax(game, depth, alpha, beta, is_computer, turn):
        print("minimax called")
        print(f" avail moves: {game.available_moves(turn)}")
        if depth == 0 or game.game_over():
            return (-1, -1), Ai.heuristic(game)

        if is_computer:
            best = [(-1, -1), -inf]
        else:
            best = [(-1, -1), +inf]


        print(f" avail moves: {  game.available_moves(turn)  }")
        for x, y in game.available_moves(turn):
            assert False, "for  ejra shod"
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
            #if beta <= alpha:
            #    break

        return best
