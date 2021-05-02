from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook

class Queen(Piece):
    symbol = "Q"
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, board, startx, starty, endx, endy, evaluate_only=True):

        if Bishop.is_valid_move(self,board,startx,starty,endx,endy) or Rook.is_valid_move(self,board,startx,starty,endx,endy):
            return True
        return False
