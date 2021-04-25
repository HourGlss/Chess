from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R"

    def is_valid_move(self, board, startx, starty, endx, endy):
        tile_is_free = board.is_tile_free(endx,endy)
        opponents_piece_is_occupying = self.attempt_capture(board, endx, endy)

        valid_movement = False
        # DOWN
        if startx == endx or endy == starty:
            # DOWN
            if starty < endy:
               stopy = None
               for y in range(starty+1, endy+1):
                   if not board.is_tile_free(endx,y):
                       stopy = y
                       break
               if stopy is None or (stopy == endy and opponents_piece_is_occupying):
                   valid_movement = True

            # UP
            elif endy < starty:
               stopy = None
               for y in range(starty-1, endy-1, -1):
                   if not board.is_tile_free(endx,y):
                       stopy = y
                       break
               if stopy is None or (stopy == endy and opponents_piece_is_occupying):
                   valid_movement = True

            # LEFT
            elif endx < startx:
               stopx = None
               for x in range(startx-1, endx-1, -1):
                   if not board.is_tile_free(x,endy):
                       stopx = x
                       break
               if stopx is None or (stopx == endx and opponents_piece_is_occupying):
                   valid_movement = True

            # RIGHT
            if startx < endx:
               stopx = None
               for x in range(startx+1, endx+1):
                   if not board.is_tile_free(x,endy):
                       stopx = x
                       break
               if stopx is None or (stopx == endx and opponents_piece_is_occupying):
                   valid_movement = True


        if (tile_is_free or opponents_piece_is_occupying) and valid_movement:
            return True
        return False