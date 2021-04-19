class Piece:
    color = None
    symbol = None

    def __init__(self, color):
        assert (color == "white" or color == "black")
        self.color = color

    def move(self):
        # print("Called from Piece")
        return None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.symbol

