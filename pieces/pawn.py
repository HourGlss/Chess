from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color, rank, file):
        super().__init__(color, rank, file)
        self.symbol = "P"

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.symbol


if __name__ == "__main__":
    p = Pawn("white", "a", 1)
    print(p.symbol)
