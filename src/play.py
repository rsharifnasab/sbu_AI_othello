
from utils.ui import Cli, QT
from othello import Othello
from utils.exc import *


if __name__ == '__main__':
    game = Othello()
    ui = Cli()

    side = -1
    while not game.game_over():
        try:
            if game.freeze(side):
                side *= -1
                continue

            ui.show_game(game)
            turn = str(Othello.piece_map(side))
            x, y = ui.get_x_y(turn)
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
