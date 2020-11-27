import numpy as np
from utils import exc


class Othello():

    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = np.zeros((8, 8), dtype=np.int)
        self.board[3, 3] = 1
        self.board[3, 4] = -1
        self.board[4, 3] = -1
        self.board[4, 4] = 1

    def get_winner(self):
        t = np.sum(self.board)
        if t > 0:
            return 1
        if t < 0:
            return -1
        return 0

    def print_board(self):
        print("   ", end="")
        for i in range(8):
            print(f"  {i}", end=" ")
        print("\n   ", end="")
        for _ in range(16):
            print("--", end="")
        print("-")
        for i in range(8):
            print(f" {i}", end=" ")
            for j in range(8):
                print("¦" + Othello.piece_map(self.board[i, j]), end="")
            print("¦")
            print("   ", end="")
            for _ in range(16):
                print("--", end="")
            print("-")

    @staticmethod
    def piece_map(x):
        return {
            1: ' ● ',
            -1: ' ○ ',
            0: '   ',
        }[x]

    def play_move(self, x, y, side):
        """ 
        Put a new piece on the board using given Args.

        Args:
            x    (int): row of the new piece on board
            y    (int): coloumn of the new piece on board
            side (int): side of the new piece

        """
        if not (-1 < x < 9 and -1 < y < 9):
            raise exc.IndexOutOfBoundException
        if self.valid_flip(x, y, side):
            self.board[x, y] = side
            self.flip(x, y, side)
            return
        raise exc.NotAnAvailableMoveException

    def flip(self, x, y, side):
        """ 
        Flip board pieces based on putting the new piece.
        """
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                if self.valid_ray(x, y, side, dx, dy):
                    self.flip_ray(x, y, side, dx, dy)

    def valid_ray(self, x, y, side, dx, dy):
        """ 
        Check if [x, y]->[x+dx, y+dy] is a valid ray for flipping pieces by putting the new piece.

        Args:
            dx   (int): relative row distance of the board square to the new piece
            dy   (int): relative coloumn distance of the board square to the new piece

        """
        # Check if the piece is on the edges of the board?
        tx = x + 2*dx
        if tx < 0 or tx > 7:
            return False
        ty = y + 2*dy
        if ty < 0 or ty > 7:
            return False
        # Check if the piece is on the same side as the new piece
        if self.board[x+dx, y+dy] != -1*side:
            return False
        # Check if there is a path that can be flipped
        while self.board[tx, ty] != side:
            if self.board[tx, ty] == 0:
                return False
            tx += dx
            ty += dy
            if tx < 0 or tx > 7:
                return False
            if ty < 0 or ty > 7:
                return False
        return True

    def flip_ray(self, x, y, side, dx, dy):
        """
        Flip pieces on [x, y]->[x+dx, y+dy] ray.
        """
        tx = x + dx
        ty = y + dy
        while self.board[tx, ty] != side:
            self.board[tx, ty] = side
            tx += dx
            ty += dy

    def valid_flip(self, x, y, side):
        """
        Check if the new piece board[x, y] has a valid flip.
        """
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                if self.valid_ray(x, y, side, dx, dy):
                    return True
        return False

    def game_over(self):
        """
        Check if there is no available move and the game is over.
        """
        for i in range(8):
            for j in range(8):
                if (self.board[i, j] == 0 and
                    (self.valid_flip(i, j, -1) or self.valid_flip(i, j, 1))):
                    return False
        return True

    def freeze(self, side):
        """
        Check if player is freezed and opposite side gets an alternate turn.
        """
        for i in range(8):
            for j in range(8):
                if self.board[i, j] == 0 and self.valid_flip(i, j, side):
                    return False
        return True
