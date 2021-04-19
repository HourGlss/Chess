from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P"

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.symbol


if __name__ == "__main__":
    p = Pawn("white")
    print(p.symbol)
