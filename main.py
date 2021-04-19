from board import Board
from pieces.pawn import Pawn


def main():
    b = Board()
    b.create_board()
    # p = Pawn("white")

    # b.board[0][1].add_piece(p2)
    b.reset_pieces()
    b.print_board()
    b.move_piece("F2 F3")

if __name__ == "__main__":
    main()
