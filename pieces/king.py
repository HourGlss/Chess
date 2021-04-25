from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "K"

    def is_valid_move(self, board, startx, starty, endx, endy):
        if starty + 1 or startx + 1 or startx - 1 or starty - 1:
            if Bishop.is_valid_move(self, board, startx, starty, endx, endy) or Rook.is_valid_move(self, board, startx,
                                                                                                   starty, endx, endy):
                return True
        else:
            return False
