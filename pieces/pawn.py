from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P"

    def is_valid_move(self, board, startx, starty, endx, endy, evaluate_only=True):
        tile_is_free = board.board[endx][endy].check_if_free()
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = False
        if not opponents_piece_is_occupying:
            if startx == endx:
                if self.color == "white":
                    if starty == 6:
                        if endy == 5:
                            valid_movement = True
                        if endy == 4 and board.board[endx][endy+1].check_if_free():
                            valid_movement = True
                    elif starty - 1 == endy:
                        valid_movement = True
                else:
                    if starty == 1:
                        if endy == 2:
                            valid_movement = True
                        if endy == 3 and board.board[endx][endy-1].check_if_free():
                            valid_movement = True
                    elif starty + 1 == endy:
                        valid_movement = True
        else:
            if startx + 1 == endx or startx - 1 == endx:
                if self.color == "white":
                    if starty - 1 == endy:
                        valid_movement = True
                else:
                    if starty + 1 == endy:
                        valid_movement = True

        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False


if __name__ == "__main__":
    p = Pawn("white")
    print(p.symbol)
