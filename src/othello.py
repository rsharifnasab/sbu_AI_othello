import numpy as np
from utils import exc


class Othello():

    p1 = -1
    p2 = 1
    pm = 2 # possible move


    def __init__(self):
        self.last_played = Othello.p2
        self.steps_passed = 0
        self.board = np.zeros((8, 8), dtype=np.int)
        self.board[3, 3] = 1
        self.board[3, 4] = -1
        self.board[4, 3] = -1
        self.board[4, 4] = 1


    def clone(self):
        c = Othello()
        # copyto(destination, source)
        np.copyto(c.board, self.board)
        c.steps_passed = self.steps_passed
        return c

    def get_winner(self):
        t = np.sum(self.board)
        if t > 0:
            return 1
        if t < 0:
            return -1
        return 0

    def __str__(self):
        moves = self.available_moves(-1 * self.last_played)
        b = self.clone().board
        for x,y in moves:
            b[x, y] = Othello.pm

        ans = "   "
        for i in range(8):
            ans += f"  {i} "
        ans += "\n   "
        ans += "--"*17 + "\n"
        for i in range(8):
            ans += f" {i} "
            for j in range(8):
                ans += "¦" + Othello.piece_map(b[i, j])
            ans += "¦\n"
            ans += "   "
            ans += "--"*17 + "\n"
        return ans

    @staticmethod
    def piece_map(x):
        return {
            Othello.p2 : ' ● ',
            Othello.p1 : ' ○ ',
            0  : '   ',
            Othello.pm : ' + ',
        }[x]

    def play_move(self, x, y, side):
        """ 
        Put a new piece on the board using given Args.

        Args:
            x    (int): row of the new piece on board
            y    (int): coloumn of the new piece on board
            side (int): side of the new piece

        """
        if x is None:
            raise exc.EndGameException
        if y is None:
            raise exc.EndGameException

        x = int(x)
        y = int(y)

        if not (-1 < x < 9 and -1 < y < 9):
            print(f"index out of.. {x} , {y}")
            raise exc.IndexOutOfBoundException

        if self.valid_flip(x, y, side):
            self.board[x, y] = side
            self.flip(x, y, side)
            self.steps_passed += 1
            self.last_played = side
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

    def available_moves(self, side):
        """
            return tuple Set of available moves
        """
        moves = []
        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                if elem == 0 and self.valid_flip(i, j, side):
                    moves.append((i, j,))
        return moves

    def game_over(self):
        """
        Check if there is no available move and the game is over.
        """
        p1 = self.available_moves(-1)
        p2 = self.available_moves(+1)
        all_moves = p1 + p2
        return len(all_moves) == 0

    def freeze(self, side):
        """
        Check if player is freezed and opposite side gets an alternate turn.
        """
        moves = self.available_moves(side)
        return len(moves) == 0
