import math


class Pawn:
    def __init__(self):
        self.color = None
        self.points = 1
        self.name = "Pawn"
        self.startingPosition = ''

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name

    def SetPosition(self, Position):
        self.startingPosition = Position


class Knight:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "Knight"

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name


class DarkBishop:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "DarkBishop"

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name


class LightBishop:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "LightBishop"

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name


class Rook:
    def __init__(self):
        self.color = None
        self.points = 5
        self.name = "Rook"

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name


class Queen:
    def __init__(self):
        self.color = None
        self.points = 9
        self.name = "Queen"

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name


class King:
    def __init__(self):
        self.color = None
        self.points = math.inf
        self.name = "King"
        self.check = False

    def SetColor(self, color):
        self.color = color

    def GetColor(self):
        return self.color

    def GetPoints(self):
        return self.points

    def GetName(self):
        return self.name

    def IsCheck(self):
        return self.checkmate

    def SetCheck(self, isCheck):
        self.checkmate = isCheck
