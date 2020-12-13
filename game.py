import pieces
import board

"""
TODO:
*PGN export
*En passant
*Castling
*Promoting pawns
*Fifty - move
rule
"""


def turn(n):
    if n % 1 == 0:
        return 'White'
    else:
        return 'Black'


class Game:
    def __init__(self):
        self.startingBoard = board.Board()
        self.points = 0
        self.moves = ''
        self.turns = 0
        self.columns = 'abcdefgh'
        self.rows = '12345678'

    def SetBoard(self):
        colors = ['White', 'Black']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        for color in colors:
            Rook = pieces.Rook()
            Rook.SetColor(color)
            Knight = pieces.Knight()
            Knight.SetColor(color)
            LightBishop = pieces.LightBishop()
            LightBishop.SetColor(color)
            Queen = pieces.Queen()
            Queen.SetColor(color)
            King = pieces.King()
            King.SetColor(color)
            DarkBishop = pieces.DarkBishop()
            DarkBishop.SetColor(color)
            Pawn = pieces.Pawn()
            Pawn.SetColor(color)

            if color == 'White':
                self.startingBoard.SetPiece(Rook, 'a1')
                self.startingBoard.SetPiece(Knight, 'b1')
                self.startingBoard.SetPiece(LightBishop, 'c1'),
                self.startingBoard.SetPiece(Queen, 'd1')
                self.startingBoard.SetPiece(King, 'e1')
                self.startingBoard.SetPiece(DarkBishop, 'f1')
                self.startingBoard.SetPiece(Knight, 'g1')
                self.startingBoard.SetPiece(Rook, 'h1')
                for x in columns:
                    self.startingBoard.SetPiece(Pawn, x + str(2))
            else:
                self.startingBoard.SetPiece(Rook, 'a8')
                self.startingBoard.SetPiece(Knight, 'b8')
                self.startingBoard.SetPiece(LightBishop, 'c8'),
                self.startingBoard.SetPiece(Queen, 'd8')
                self.startingBoard.SetPiece(King, 'e8')
                self.startingBoard.SetPiece(DarkBishop, 'f8')
                self.startingBoard.SetPiece(Knight, 'g8')
                self.startingBoard.SetPiece(Rook, 'h8')
                for x in columns:
                    self.startingBoard.SetPiece(Pawn, x + str(7))
                    Pawn.SetPosition(x)

    def PrintGame(self):
        self.startingBoard.PrintBoard()

    def LegalMove(self, move):
        """
        Format is (piece, startPosition, endPosition)
        """
        pieceName = move[0]
        startPosition = move[1]
        endPosition = move[2]

        if self.startingBoard.GetPiece(startPosition).GetName() is not pieceName:
            return False

        if turn(self.turns) == 'White':
            if startPosition == endPosition:
                return False
            elif startPosition[0].lower() not in self.columns and endPosition[0].lower() not in self.columns:
                return False
            if pieceName == 'Pawn':
                if endPosition[-1] - startPosition[-1] == 1:
                    if endPosition[0] == startPosition[0] and self.startingBoard.GetPiece(startPosition) is None:
                        return True
                    elif (endPosition[0] - startPosition[0]) == 2 and \
                            self.startingBoard.GetPiece(startPosition[0] + str(int(startPosition[-1] - 1))) is not None:
                        return True
                    #TODO FIX THIS
                    elif endPosition[0] != startPosition[0] and self.startingBoard.GetPiece(endPosition) is None \
                            and self.startingBoard.GetPiece(endPosition):



        if self.rows.find(startPosition[0].lower()) + self.rows.find(endPosition[0].lower()) <= 2:

        if pieceName == 'Pawn':
            if turn(self.turns) == 'White':
                if endPosition[-1] - startPosition[-1] == 1:
                    if endPosition[0] == startPosition[0] and self.startingBoard.GetPiece(startPosition) is None:
                        return True
                    elif endPosition[0] != startPosition[0] and self.startingBoard.GetPiece(endPosition) is not None \
                            and self.startingBoard.GetPiece(endPosition).GetColor() == 'Black':
                        return True
                    elif endPosition[0] != startPosition[0] and self.startingBoard.GetPiece(endPosition) is None \
                            and self.startingBoard.GetPiece(endPosition):
                    else:
                        return False
                elif startPosition[-1] == 2 and turn(self.turns) and (endPosition[-1] - startPosition[-1]) == 2:
                    return True
                elif
                else:
                    return False
            elif startPosition[-1] == 7 and self.startingBoard.GetPiece(startPosition).GetColor() == 'Black' \
                    and (startPosition[-1] - endPosition[-1]) == 2:
                legal = True

    def NewMove(self, move):
        self.startingBoard.DelPiece(move[1])
        self.startingBoard.DelPiece(move[2])
        self.startingBoard.SetPiece(move[0], move[2])
        self.turns += 0.5
