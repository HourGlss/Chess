from colorama import Fore, Back, Style

from tile import Tile
from config import Config
# Import all the pieces
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class Board:
    board = None

    def __init__(self):
        pass

    def create_board(self):
        self.board = []
        color = "white"
        for x in range(Config.BOARD_SIZE):
            current = []
            for y in range(Config.BOARD_SIZE):
                temp = Tile(x, y, color)
                current.append(temp)
                if color == "white":
                    color = "black"
                else:
                    color = "white"
            if color == "white":
                color = "black"
            else:
                color = "white"
            self.board.append(current)

    def reset_pieces(self):

        # p2 = Pawn("black")
        # b.board[5][6].add_piece(p)

        # WHITE PAWNS
        color = "white"
        for i in range(Config.BOARD_SIZE):
            p = Pawn(color)
            self.board[i][6].add_piece(p)
        # Other white pieces
        pieces = [Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color),
                  Rook(color)]
        for i in range(len(pieces)):
            self.board[i][7].add_piece(pieces[i])

        # BLACK PAWNS
        color = "black"
        for i in range(Config.BOARD_SIZE):
            p = Pawn(color)
            self.board[i][1].add_piece(p)
        # Other black pieces
        pieces = [
            Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color),
            Rook(color)]
        for i in range(len(pieces)):
            self.board[i][0].add_piece(pieces[i])

    def is_piece_under_attack(self, piecex, piecey):
        piece = self.board[piecex][piecey].get_piece()
        if piece is not None:
            for x in range(Config.BOARD_SIZE):
                for y in range(Config.BOARD_SIZE):
                    pass



    def custom_piece_placement(self):
        color = "white"
        n = Knight(color)
        r = Rook(color)
        q = Queen(color)
        b = Bishop(color)
        k = King(color)

        self.board[2][6].add_piece(r)
        self.board[5][3].add_piece(r)
        self.board[5][1].add_piece(b)
        self.board[3][1].add_piece(q)
        self.board[4][3].add_piece(n)
        self.board[1][1].add_piece(k)

        color = "black"
        p = Pawn(color)
        self.board[2][3].add_piece(p)
        self.board[5][6].add_piece(p)
        self.board[1][5].add_piece(p)

    def print_board(self, selected=False, parsed_user_input=None):
        selx, sely, piece = None, None, None

        if selected:
            selx, sely = parsed_user_input
            piece = self.board[selx][sely].get_piece()

        if not selected or (selected and piece is None):
            y = 0
            # THIS IS FOR DEBUG
            # TODO COMMENT THIS OUT FOR PROD
            print(f"\t{Fore.GREEN}", end="")
            for i in range(Config.BOARD_SIZE):
                print(f" {i} ", end="")
            print(f"{Style.RESET_ALL}")
            # END DEBUG PRINT SECTION

            for rank in Config.ranks:
                print(f"{rank:2}", end="\t")
                x = 0
                for file in Config.files:
                    print(self.board[x][y], end="")
                    x += 1
                # THIS IS FOR DEBUG
                # TODO COMMENT THIS OUT FOR PROD
                print(f" {Fore.GREEN}{y}{Style.RESET_ALL}")
                # END DEBUG PRINT SECTION
                y += 1
            print("\t", end="")
            for file in Config.files:
                print(f" {file} ", end="")
            print()
        elif selected and parsed_user_input is not None:

            # CHANGE THE BACKGROUND COLOR
            for y in range(Config.BOARD_SIZE):
                for x in range(Config.BOARD_SIZE):
                    if piece.is_valid_move(self, selx, sely, x, y):
                        if self.if_tile_is_free(x, y):
                            self.board[x][y].background_color = Back.LIGHTYELLOW_EX
                        else:
                            self.board[x][y].background_color = Back.LIGHTCYAN_EX

            # ACTUALLY PRINT THE BOARD
            y = 0
            for rank in Config.ranks:
                print(f"{rank:2}", end="\t")
                x = 0
                for file in Config.files:
                    print(self.board[x][y], end="")
                    x += 1
                y += 1
                print()
            print("\t", end="")
            for file in Config.files:
                print(f" {file} ", end="")
            print()

            # RESET ALL THE BACKGROUND COLORS
            for y in range(Config.BOARD_SIZE):
                for x in range(Config.BOARD_SIZE):
                    self.board[x][y].set_background_color()

    def if_tile_is_free(self, x, y):
        return self.board[x][y].check_if_free()

    def get_piece_at(self, x, y):
        return self.board[x][y].get_piece()

    def move_piece(self, player_color, input_from_user):
        if input_from_user is not None:
            startx, starty, endx, endy = input_from_user
        else:
            print("Bad input!")
            return False
        # print(f"({startx},{starty}) -> ({endx},{endy})")
        piece = self.board[startx][starty].get_piece()
        if piece.color != player_color:
            print("That is not your piece to move!")
            return False
        if piece is not None:
            if piece.is_valid_move(self, startx, starty, endx, endy):
                self.board[startx][starty].remove_piece()
                self.board[endx][endy].add_piece(piece)
                return True
            else:
                print("MOVE IS NOT VALID - PIECE CANT MOVE THAT WAY")
                return False
        else:
            print("MOVE IS NOT VALID - NO PIECE THERE")
            return False


if __name__ == "__main__":
    b = Board()
    b.create_board()
