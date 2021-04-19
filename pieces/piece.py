class Piece:
    color = None
    symbol = None

    def __init__(self, color, rank, file):
        assert (color == "white" or color == "black")
        self.color = color
        self.rank = rank
        self.file = file


    def move(self):
        print("Called from Piece")
        return None

