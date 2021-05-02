from pieces.piece import Piece


class Bishop(Piece):
    symbol = "B"
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self:Piece, board, startx, starty, endx, endy, evaluate_only=True):
        tile_is_free = board.is_tile_free(endx, endy)
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = False
        if self.forms_x(startx, starty, endx, endy):
            # DOWN, RIGHT
            if starty < endy and startx < endx:
                stopy = None
                stopx = None
                x = startx + 1
                for y in range(starty + 1, endy + 1):
                    if not board.is_tile_free(x, y):
                        stopy = y
                        stopx = x
                        break
                    x += 1
                if (stopy is None and stopx is None) or (
                        stopy == endy and stopx == endx and opponents_piece_is_occupying):
                    valid_movement = True

            # down left
            elif starty < endy and endx < startx:
                stopy = None
                stopx = None
                x = startx - 1
                for y in range(starty + 1, endy + 1):
                    if not board.is_tile_free(x, y):
                        stopy = y
                        stopx = x
                        break
                    x -= 1
                if (stopy is None and stopx is None) or (
                        stopy == endy and stopx == endx and opponents_piece_is_occupying):
                    valid_movement = True

            # up right
            elif endy < starty and startx < endx:
                stopy = None
                stopx = None
                x = startx + 1
                for y in range(starty - 1, endy - 1, -1):
                    if not board.is_tile_free(x, y):
                        stopy = y
                        stopx = x
                        break
                    x += 1
                if (stopy is None and stopx is None) or (
                        stopy == endy and stopx == endx and opponents_piece_is_occupying):
                    valid_movement = True

            # up left
            elif endy < starty and startx > endx:
                stopy = None
                stopx = None
                x = startx - 1
                for y in range(starty - 1, endy - 1, -1):
                    if not board.is_tile_free(x, y):
                        stopy = y
                        stopx = x
                        break
                    x -= 1
                if (stopy is None and stopx is None) or (
                        stopy == endy and stopx == endx and opponents_piece_is_occupying):
                    valid_movement = True

        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False
