import math


class Pawn:
    def __init__(self):
        self.color = None
        self.points = 1
        self.name = "Pawn"

    def SetColor(self, color):
        self.color = color


class Knight:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "Knight"

    def SetColor(self, color):
        self.color = color

    def GetPoints(self):
        return self.points

class DarkBishop:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "DarkBishop"

    def SetColor(self, color):
        self.color = color


class LightBishop:
    def __init__(self):
        self.color = None
        self.points = 3
        self.name = "LightBishop"

    def SetColor(self, color):
        self.color = color


class Rook:
    def __init__(self):
        self.color = None
        self.points = 5
        self.name = "Rook"

    def SetColor(self, color):
        self.color = color


class Queen:
    def __init__(self):
        self.color = None
        self.points = 9
        self.name = "Queen"

    def SetColor(self, color):
        self.color = color


class King:
    def __init__(self):
        self.color = None
        self.points = math.inf
        self.name = "King"

    def SetColor(self, color):
        self.color = color
