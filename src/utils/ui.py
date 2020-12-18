from sys import exit as sys_exit
from abc import ABC, abstractmethod
from typing import List, Set, Dict, Tuple, Optional

from zenipy.zenipy import message, scale, warning
from zenipy.zenipy import error as qt_error

from utils.color import colors


class Ui(ABC):
    @staticmethod
    @abstractmethod
    def show_game(game):
        pass

    @staticmethod
    @abstractmethod
    def get_x_y(turn):
        pass

    @staticmethod
    @abstractmethod
    def error(exception):
        pass

    @staticmethod
    @abstractmethod
    def exception(exception):
        pass

    @staticmethod
    @abstractmethod
    def tie():
        pass

    @staticmethod
    @abstractmethod
    def win(winner):
        pass

    @staticmethod
    @abstractmethod
    def alert_freeze_game():
        pass

    @staticmethod
    @abstractmethod
    def ai_think(turn):
        pass


class Cli():
    @staticmethod
    def show_game(game):
        print(colors.CLEAR)
        print(game)

    @staticmethod
    def get_x_y(turn):
        print(f"{turn} turn")
        x, y = input("enter x, y: ").split()
        return (int(x), int(y))

    @staticmethod
    def error(exception):
        print(f"{colors.BOLD}{colors.RED}{exception}{colors.RESET}")
        sys_exit(1)

    @staticmethod
    def exception(exception):
        print(f"{colors.BOLD}{colors.RED}{exception}{colors.RESET}")
        input("press enter and then try again.")

    @staticmethod
    def tie():
        print(f'{colors.BOLD}{colors.GREEN}The game is tie{colors.RESET}\n')

    @staticmethod
    def win(winner):
        print(f'{colors.BOLD}{colors.GREEN}Winner is: {colors.RESET}{winner}\n')

    @staticmethod
    def alert_freeze_game():
        print(f'{colors.BOLD}game is freezed!{colors.RESET}\n')

    @staticmethod
    def ai_think(turn):
        print(f"ai is thinikng... as {turn}")


class QT():
    @staticmethod
    def show_game(board):
        print(colors.CLEAR)
        print(board)

    @staticmethod
    def get_x_y(turn):
        x = scale(text=f"{turn} x?", min=0, max=7)
        y = scale(text=f"{turn} y?", min=0, max=7)
        return (x, y)

    @staticmethod
    def error(exception):
        qt_error(text=str(exception))
        sys_exit(1)

    @staticmethod
    def exception(exception):
        warning(text=f"{exception}\npress enter and then try again.")

    @staticmethod
    def tie():
        message(text="The game is Tie")

    @staticmethod
    def win(winner):
        message(text=f"Winner is:{winner}")

    @staticmethod
    def alert_freeze_game():
        message("freeze game", text="the game is freezed")

    @staticmethod
    def ai_think(turn):
        message("ai turn", text="press ok to start thinking")
        print(f"ai is thinikng... as {turn}")
