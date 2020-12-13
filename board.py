import numpy as np
import pandas


def LetterToNumber(letter):
    # switcher = {
    #     'a': 8,
    #     'b': 7,
    #     'c': 6,
    #     'd': 5,
    #     'e': 4,
    #     'f': 3,
    #     'g': 2,
    #     'h': 1
    # }
    switcher = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }
    return switcher.get(letter)


def ObjectToSymbol(PieceObject):
    if PieceObject is None:
        return '◼'
    piece = PieceObject.GetName()
    color = PieceObject.GetColor()
    whiteSwitcher = {
        'King': '♔',
        'Queen': '♕',
        'Rook': '♖',
        'DarkBishop': '♗',
        'LightBishop': '♗',
        'Knight': '♘',
        'Pawn': '♙'
    }
    blackSwitcher = {
        'King': '♚',
        'Queen': '♛',
        'Rook': '♜',
        'DarkBishop': '♝',
        'LightBishop': '♝',
        'Knight': '♞',
        'Pawn': '♟'
    }
    if color == 'White':
        return whiteSwitcher.get(piece)
    else:
        return blackSwitcher.get(piece)


class Board:
    def __init__(self):
        self.board = np.empty((8, 8), dtype=object)
        self.bPieceCount = 0
        self.wPieceCount = 0

    def PrintBoard(self):
        row_labels = ['8', '7', '6', '5', '4', '3', '2', '1']
        for row_label, row in zip(row_labels, self.board):
            print('%s [%s]' % (row_label, ' '.join(' %03s' % ObjectToSymbol(i) for i in row)))
        print('  [   A     B     C    D     E    F     G     H]')

    def SetPiece(self, piece, position):
        row = int(LetterToNumber(position[0]))
        column = int(position[-1])
        self.board[column - 1][row - 1] = piece

    def DelPiece(self, position):
        row = int(LetterToNumber(position[0]))
        column = int(position[-1])
        self.board[column - 1][row - 1] = None
