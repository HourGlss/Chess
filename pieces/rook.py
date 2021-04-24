from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R"

    def is_valid_move(self, board, startx, starty, endx, endy):
        tile_is_free = board.board[endx][endy].check_if_free()
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = False
        # DOWN
        if starty < endy:
           if startx == endx:
               for i in range(starty+1, endy+1):
                   print(f'this is endx {endx} i {i}')
                   if not board.board[endx][i].check_if_free():
                       return False
                   elif self.attempt_capture(board, endx, i):
                       return True

               valid_movement = True
        # UP
        # IF IM MOVING UP
            # IF THERES NOTHING IN THE WAY
                # VALID MOVEMENT IS TRUE

        # LEFT
        # IF IM MOVING LEFT
            # IF THERES NOTHING IN THE WAY
                # VALID MOVEMENT IS TRUE
        # RIGHT
        # IF IM MOVING RIGHT
            # IF THERES NOTHING IN THE WAY
                # VALID MOVEMENT IS TRUE

        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False