import pieces
import board


class Game:
    def __init__(self):
        self.StartingBoard = board.Board()
        self.checkmate = False
        self.game = board.Board()

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
                self.StartingBoard.SetPiece(Rook, 'a1')
                self.StartingBoard.SetPiece(Knight, 'b1')
                self.StartingBoard.SetPiece(LightBishop, 'c1'),
                self.StartingBoard.SetPiece(Queen, 'd1')
                self.StartingBoard.SetPiece(King, 'e1')
                self.StartingBoard.SetPiece(DarkBishop, 'f1')
                self.StartingBoard.SetPiece(Knight, 'g1')
                self.StartingBoard.SetPiece(Rook, 'h1')
                for x in columns:
                    self.StartingBoard.SetPiece(Pawn, x + str(2))
            else:
                self.StartingBoard.SetPiece(Rook, 'a8')
                self.StartingBoard.SetPiece(Knight, 'b8')
                self.StartingBoard.SetPiece(LightBishop, 'c8'),
                self.StartingBoard.SetPiece(Queen, 'd8')
                self.StartingBoard.SetPiece(King, 'e8')
                self.StartingBoard.SetPiece(DarkBishop, 'f8')
                self.StartingBoard.SetPiece(Knight, 'g8')
                self.StartingBoard.SetPiece(Rook, 'h8')
                for x in columns:
                    self.StartingBoard.SetPiece(Pawn, x + str(7))
                    Pawn.SetPosition(x)

    def PrintGame(self):
        self.StartingBoard.PrintBoard()
