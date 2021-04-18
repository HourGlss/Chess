class Piece:
    owner = None
    location = None
    symbol = None

    def __init__(self, owner, rank, file):
        self.owner = owner
        self.rank = rank
        self.file = file


    def move(self):
        print("Called from Piece")
        return None
