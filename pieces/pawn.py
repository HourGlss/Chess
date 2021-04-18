from piece import Piece


class Pawn(Piece):
    def __init__(self, owner, rank, file):
        super().__init__(owner, rank, file)
        self.symbol = "P"


if __name__ == "__main__":
    p = Pawn("white", "a", 1)
    print(p.symbol)
