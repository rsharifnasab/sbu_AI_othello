from utils.color import colors


class GameException(Exception):
    code = 0
    message = ''

    def __init__(self, for_api=True, message='', status=0):
        self.for_api = for_api
        if message:
            self.message = message
        if status:
            self.status = status

    def __str__(self):
        return f'{colors.BOLD}{colors.RED}Error{self.code}- {self.message}{colors.RESET}'


class IndexOutOfBoundException(GameException):
    code=101
    message='Index is out of bounds!'

class NotAnAvailableMoveException(GameException):
    code=102
    message='It isn\'t an available move!'


class EndGameException(GameException):
    code=103
    message='you left the game'
