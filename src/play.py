from sys import exit as sys_exit
from othello import Othello
from utils.exc import GameException
from utils.color import colors

if __name__ == '__main__':
    game = Othello()
    side = -1
    while not game.game_over():
        try:
            if game.freeze(side):
                side *= -1
                continue
            print(colors.CLEAR)
            game.print_board()
            print(f"Turn: {Othello.piece_map(side)}")
            x = int(input('row: '))
            y = int(input('coloumn: '))
            game.play_move(x, y, side)
            side *= -1
        except GameException as exception:
            print(exception)
            input("press enter and then try again.")
        except ValueError as ve:
            input("bad input, press enter and try again")
        except KeyboardInterrupt:
            print("\ngoodbye")
            sys_exit(1)
    print(colors.CLEAR)
    game.print_board()
    winner = game.get_winner()
    if winner == 0:
        print(f'{colors.BOLD}{colors.GREEN}The game is tie{colors.RESET}\n')
    else:
        print(
            f'{colors.BOLD}{colors.GREEN}Winner is: {colors.RESET}{Othello.piece_map(winner)}\n')
