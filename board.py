import pieces
import numpy as np


def LetterToNumber(letter):
    switcher = {
        'a': 8,
        'b': 7,
        'c': 6,
        'd': 5,
        'e': 4,
        'f': 3,
        'g': 2,
        'h': 1
    }
    return switcher.get(letter)


class Board:
    def __init__(self):
        self.board = np.empty((8, 8), dtype=object)
        self.bPieceCount = 0
        self.wPieceCount = 0

    def PrintBoard(self):
        print('-' * 45)
        for row in self.board:
            print(*row, sep=' | ')
            print('-' * 45)

    def SetPiece(self, piece, position):
        row = int(LetterToNumber(position[0]))
        column = int(position[-1])
        self.board[row - 1][column - 1] = piece
