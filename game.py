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
        self.piecesNames = ['Pawn', 'Knight', 'Darkbishop', 'Lightbishop', 'Rook', 'Queen', 'King']

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

    def LegalMove(self, move: tuple[:3]):
        """
        Format is a tuple (piece, startPosition, endPosition)
        Example: ('Pawn', 'e2', 'e4')
        """
        pieceName: str = move[0].capitalize()
        startPosition: str = move[1].lower()
        endPosition: str = move[2].lower()

        if self.startingBoard.GetPiece(startPosition).GetName() is not pieceName:
            raise Exception('Piece is not on starting position.')

        if startPosition == endPosition:
            raise Exception('Piece has not moved.')

        if startPosition[0] not in self.columns and endPosition[0] not in self.columns \
                and 1 <= int(startPosition[1]) <= 8 and 1 <= int(endPosition[1]) <= 8:
            raise Exception('Piece\'s start or end position is not on the board.')

        if pieceName not in self.piecesNames:
            raise Exception('Not a valid Piece name')

        if turn(self.turns) == 'White':
            # Code for legal moves for a pawn
            if pieceName == self.piecesNames[0]:

                if endPosition[0] == startPosition[0]:  # If on the same file it means pawn is not capturing

                    if int(endPosition[1]) - int(startPosition[1]) == 1:  # If the pawn moves up 1 square

                        if self.startingBoard.GetPiece(endPosition) is None:
                            # Test if there is no piece on the end position then it is a legal move
                            return True, {'EnPassant': False}
                        else:
                            raise Exception(f'There is a {self.startingBoard.GetPiece(endPosition)} '
                                            f'on {endPosition} blocking your Pawn')

                    elif int(endPosition[1]) - int(startPosition[1]) == 2:
                        # Test if the two squares above the pawn are empty and the pawn is on the second rank
                        if self.startingBoard.GetPiece(startPosition[0] + str(int(startPosition[1]) + 1)) is None \
                                and self.startingBoard.GetPiece(endPosition) is None \
                                and startPosition[1] == '2':
                            return True, {'EnPassant': True}
                        else:
                            raise Exception('Invalid Move')
                    else:
                        raise Exception('Invalid Move')
                elif abs(self.columns.find(endPosition[0]) - self.columns.find(startPosition[0])) == 1:

                    if self.startingBoard.GetPiece(endPosition) is not None \
                            and self.startingBoard.GetPiece(endPosition).GetColor() == 'Black':

                        return True, {'EnPassant': False}

                    elif self.startingBoard.GetPiece(endPosition) is None:
                        testEnPassant = self.startingBoard.GetPiece(endPosition[0] + str(int(endPosition[1]) - 1))
                        if testEnPassant is not None and testEnPassant.GetName() == 'Pawn' \
                                and testEnPassant.GetEnPassant() is True:
                            self.startingBoard.DelPiece(endPosition[0] + str(int(endPosition[1]) - 1))
                            return True, {'EnPassant': False}
                        else:
                            raise Exception('No piece to capture')
                    else:
                        raise Exception('Invalid Move')
                else:
                    raise Exception('Invalid Move')

    def NewMove(self, move):
        legalMove = self.LegalMove(move)
        if type(tuple) == type(legalMove):
            if 'EnPassant' in legalMove[1]:
                self.startingBoard.DelPiece(move[1])
                self.startingBoard.DelPiece(move[2])
                self.startingBoard.SetPiece(move[0], move[2])
                self.turns += 0.5
        if self.LegalMove(move):
            self.startingBoard.DelPiece(move[1])
            self.startingBoard.DelPiece(move[2])
            self.startingBoard.SetPiece(move[0], move[2])
            self.turns += 0.5
