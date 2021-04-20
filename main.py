from board import Board
import colorama
import sys
def main():
    colorama.init()
    b = Board()
    b.create_board()
    # p = Pawn("white")

    # b.board[0][1].add_piece(p2)
    b.reset_pieces()

    user_input = ""
    clear_screen()
    while user_input != "Q":
        b.print_board()
        user_input = input("FROM TO or Q\n")

        if user_input != "Q":
            while not b.move_piece(user_input):
                user_input = input("FROM TO or Q\n")

        clear_screen()




def clear_screen():
    # ONE OF THESE WORKS
    print('\u001b[2J', end="")
    colorama.ansi.clear_screen()
    sys.stdout.write('\u001b[2J')

if __name__ == "__main__":
    main()
