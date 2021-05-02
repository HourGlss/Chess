from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook


class King(Piece):
    symbol = "K"

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, board, startx, starty, endx, endy, evaluate_only=True):
        if self.color == "white":
            look_for_color = "black"
        else:
            look_for_color = "white"
        if (startx == endx or startx+1 == endx or startx-1 == endx) and (starty + 1== endy or starty - 1 == endy or starty==endy):
            if Bishop.is_valid_move(self, board, startx, starty, endx, endy) or Rook.is_valid_move(self, board, startx,
                                                                                                   starty, endx, endy):
                if not evaluate_only:
                    self.moved = True
                if board.check_if_tile_under_attack(endx,endy,look_for_color):
                    return False
                return True
        elif starty == endy and abs(endx-startx) == 2:
            # FUCKING CASTLING
            if not self.moved:
                look_for_color = None

                if endx < startx:
                    # LEFT
                    # print("Castle to the left")

                    if not board.check_if_tile_under_attack(startx, starty, look_for_color):
                        if not board.check_if_tile_under_attack(startx - 1, starty, look_for_color) and board.is_tile_free(startx - 1, starty):
                            if not board.check_if_tile_under_attack(startx - 2, starty,look_for_color) and board.is_tile_free(startx - 2,starty):
                                if board.is_tile_free(startx-3,starty):
                                    other_piece = board.get_piece_at(0, starty)
                                    if other_piece is not None and not other_piece.moved and isinstance(other_piece, Rook):
                                        if not evaluate_only:
                                            board.board[startx - 4][starty].remove_piece()
                                            board.board[startx - 1][endy].add_piece(other_piece)
                                        if board.check_if_tile_under_attack(endx, endy, look_for_color):
                                            return False
                                        return True

                if startx < endx:
                    # RIGHT
                    # print("Castle to the right")

                    if not board.check_if_tile_under_attack(startx,starty,look_for_color):
                        if not board.check_if_tile_under_attack(startx+1,starty,look_for_color) and board.is_tile_free(startx+1,starty):
                            if not board.check_if_tile_under_attack(startx+2,starty,look_for_color) and board.is_tile_free(startx+2,starty):
                                other_piece = board.get_piece_at(7,starty)
                                if other_piece is not None and not other_piece.moved and isinstance(other_piece,Rook):
                                    if not evaluate_only:
                                        print("Yes move it!")
                                        board.board[startx+3][starty].remove_piece()
                                        board.board[startx+1][endy].add_piece(other_piece)
                                    if board.check_if_tile_under_attack(endx, endy, look_for_color):
                                        return False
                                    return True
        else:
            return False
