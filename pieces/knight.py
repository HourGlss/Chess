from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "N"

    def is_valid_move(self, board, startx, starty, endx, endy, evaluate_only=True):
        tile_is_free = board.board[endx][endy].check_if_free()
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = ((endx == startx-1 or endx == startx+1) and (endy == starty+2 or endy == starty-2)) or ((endy == starty+1 or endy == starty-1) and (endx == startx+2 or endx == startx-2))
        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False
