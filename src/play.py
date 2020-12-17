#!/usr/bin/python3
from utils.ui import Cli, QT
from othello import Othello
from utils.exc import *
from utils.argparse import ui_chooser, player_creator


def main():

    p1 = -1
    p2 = 1

    game = Othello()
    ui = ui_chooser()
    players = player_creator()

    side = p1
    while not game.game_over():
        if game.freeze(side):
            side *= -1
            continue

        curr_player = players[0 if side == p1 else 1]
        try:
            turn = str(Othello.piece_map(not side))
            x, y = curr_player.get_move(game, ui, turn)
            game.play_move(x, y, side)

            side *= -1

        except EndGameException as exception:
            ui.error(exception)
        except GameException as exception:
            ui.exception(exception)
        except ValueError as ve:
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
