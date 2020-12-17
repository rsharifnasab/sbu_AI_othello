from utils.ui import Cli, QT
from othello import Othello
from utils.exc import *
from utils.argparse import ui_chooser, player_creator


def change_side(old_side):
    return {
            "player1" : "player2",
            "player2" : "player1",
        }.get(old_side)


if __name__ == "__main__":
    game = Othello()
    ui = ui_chooser()
    players = player_creator()

    side = -1
    while not game.game_over():
        if game.freeze(side):
            side *= -1
            continue

        if side == 1: #user 
            ui.show_game(game)
            try:
                turn = str(Othello.piece_map(side*-1))
                x, y = ui.get_x_y(turn)
                game.play_move(x, y, side)

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
