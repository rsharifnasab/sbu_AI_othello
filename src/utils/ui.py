from zenipy.zenipy import message, scale
from utils.color import colors
from sys import exit as sys_exit


class Cli():

    @staticmethod
    def show_game(game):
            print(colors.CLEAR)
            print(game)

    @staticmethod
    def get_x_y(turn):
        print(f"{turn} turn")
        x, y = input("enter x, y: ").split()
        return (int(x),int(y))

    @staticmethod
    def error(exception):
        print(str(exception))
        sys_exit(1)

    @staticmethod
    def exception(exception):
        print(str(exception))
        input("press enter and then try again.")

    @staticmethod
    def tie():
        print(f'{colors.BOLD}{colors.GREEN}The game is tie{colors.RESET}\n')

    @staticmethod
    def win(winner):
        print(f'{colors.BOLD}{colors.GREEN}Winner is: {colors.RESET}{winner}\n')



class QT():
    @staticmethod
    def show_game(board):
            print(colors.CLEAR)
            print(game)

    @staticmethod
    def get_x_y(turn):
        x = scale(text=f"{turn} x?", min=0, max=7)
        y = scale(text=f"{turn} y?", min=0, max=7)
        return (x,y)
