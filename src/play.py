#!/usr/bin/python3
from typing import List, Set, Dict, Tuple, Optional

from utils.ui import Ui
from utils.agent import Agent
from othello import Othello
from utils.exc import *
from utils.argparse import ui_chooser, player_creator


def main():

    p1: int = -1
    p2: int = 1

    game: Othello = Othello()
    ui: Ui = ui_chooser()
    players: Tuple[Agent, Agent] = player_creator()

    side : int = p1
    while not game.game_over():
        if game.freeze(side):
            if game.freeze(-1 * side):
                ui.alert_freeze_game()
                break
            side *= -1
            continue

        curr_player : Agent = players[0 if side == p1 else 1]
        try:
            game.available_moves(side)
            x, y = curr_player.get_move(game, ui, side)
            game.play_move(x, y, side)

            # only if everything is ok
            side *= -1

        except EndGameException as exception:
            ui.error(exception)
        except GameException as exception:
            ui.exception(exception)
        except ValueError as ve:
            if "unpack" not in str(ve):
                raise ve
            ui.exception(ve)
        except KeyboardInterrupt:
            ui.error("\nterminated by Ctrl-C")

    ui.show_game(game)
    winner = game.get_winner()
    if winner == 0:
        ui.tie()
    else:
        ui.win(Othello.piece_map(winner))


if __name__ == "__main__":
    main()
