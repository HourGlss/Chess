from board import Board
from pieces.pawn import Pawn


def main():
    b = Board()
    b.create_board()
    p = Pawn("white")
    p2 = Pawn("black")

    b.board[5][6].add_piece(p)
    b.board[0][1].add_piece(p2)
    b.print_board()

if __name__ == "__main__":
    main()
