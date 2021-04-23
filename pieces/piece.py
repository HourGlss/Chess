class Piece:
    color = None
    symbol = None

    def __init__(self, color):
        assert (color == "white" or color == "black")
        self.color = color

    def is_valid_move(self,board,startx,starty,endx,endy):
        # print("Called from Piece")
        return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.symbol

