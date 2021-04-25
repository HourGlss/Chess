from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "Q"

    def is_valid_move(self, board, startx, starty, endx, endy):
        if Bishop.is_valid_move(self,board,startx,starty,endx,endy) or Rook.is_valid_move(self,board,startx,starty,endx,endy):
            return True
        return False
