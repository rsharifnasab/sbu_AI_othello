import os
from othello import Othello
from utils import exc
from utils.color import colors

if __name__ == '__main__':
    game = Othello()
    side = -1
    while not game.game_over():
        try:
            if game.freeze(side):
                side *= -1
                continue
            print("\033c")
            game.print_board()
            print(f"Turn: {Othello.piece_map(side)}")
            x = int(input('row: '))
            y = int(input('coloumn: '))
            game.play_move(x, y, side)
            side *= -1
        except Exception as exception:
            print(exception)
            input("press enter and then try again.")
    print("\033c")
    game.print_board()
    winner = game.get_winner()
    if winner == 0:
        print(u'{}{}The game is tie{}'.format(colors.BOLD, colors.GREEN, colors.RESET), end='\n\n')
    else:
        print(u'{}{}The winner is: {}{}'.format(colors.BOLD, colors.GREEN, colors.RESET, Othello.piece_map(winner)), end='\n\n')
