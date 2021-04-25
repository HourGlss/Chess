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
        if startx == endx or endy == starty:
            # DOWN
            if starty < endy:
               stopy = None
               for y in range(starty+1, endy+1):
                   if not board.board[endx][y].check_if_free():
                       stopy = y
                       break
               if stopy is None or (stopy == endy and opponents_piece_is_occupying):
                   valid_movement = True

            # UP
            elif starty > endy:
               stopy = None
               for y in range(endy, starty):
                   if not board.board[endx][y].check_if_free():
                       stopy = y
                       break
               if stopy is None or (stopy == endy and opponents_piece_is_occupying):
                   valid_movement = True

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