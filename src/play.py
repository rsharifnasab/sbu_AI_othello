from utils.ui import Cli, QT
from othello import Othello
from utils.exc import *
import sys


if __name__ == '__main__':
    game = Othello()
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-c', '--cli']:
            ui = Cli()
        elif sys.argv[1] in ['-g', '--gui']:
            ui = QT()
        else:
            print(f"""error: unknown option `{sys.argv[1]}\'
options:

    -c, --cli            command line interface
    -g, --gui            graphical user interface
            """)
            exit()
    else:
            ui = QT()

    side = -1
    while not game.game_over():
        try:
            if game.freeze(side):
                side *= -1
                continue

            ui.show_game(game)
            turn = str(Othello.piece_map(side*-1))
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
