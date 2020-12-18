#!/usr/bin/python3
from utils.ui import Ui
from othello import Othello
from utils.exc import *
from utils.argparse import ui_chooser, player_creator


def main():

    p1 : int = -1
    p2 : int = 1

    game : Othello = Othello()
    ui : Ui = ui_chooser()
    players : Tuple[Agent, Agent] = player_creator()

    side = p1
    while not game.game_over():
        if game.freeze(side):
            if game.freeze(-1 * side):
                ui.alert_freeze_game()
                break
            side *= -1
            continue

        curr_player = players[0 if side == p1 else 1]
        try:
            turn = str(Othello.piece_map(not side))
            game.available_moves(side)
            x, y = curr_player.get_move(game, ui, side)
            game.play_move(x, y, side)

            side *= -1

        except EndGameException as exception:
            ui.error(exception)
        except GameException as exception:
            ui.exception(exception)
     #   except ValueError as ve:
     #       ui.exception(ve)
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
