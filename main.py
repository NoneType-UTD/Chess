import board
import pieces

if __name__ == '__main__':
    knight = pieces.Knight()
    test = board.Board()
    test.SetPiece(knight, 'a1')
    # print(type(knight))
    test.PrintBoard()