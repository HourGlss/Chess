from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "B"

    def is_valid_move(self, board, startx, starty, endx, endy):
        tile_is_free = board.is_tile_free(endx, endy)
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = False
        if self.forms_x(startx, starty, endx, endy):
            # DOWN, RIGHT
            if starty < endy and startx < endx:
                stopy = None
                stopx = None
                x = startx
                for y in range(starty + 1, endy + 1):
                    if not board.is_tile_free(endx, y):
                        stopy = y
                        stopx = x
                        break
                    x += 1
                if (stopy is None and stopx is None) or (
                        stopy == endy and stopx == endx and opponents_piece_is_occupying):
                    valid_movement = True

            # down left

            # up right

            # up left


        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False
