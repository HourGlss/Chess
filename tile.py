import colorama
from colorama import Fore, Back, Style


class Tile:
    x = None
    y = None
    piece = None
    chess_color = None
    background_color = None

    def __init__(self, x, y, chess_color):
        self.x = x
        self.y = y
        assert (chess_color == "white" or chess_color == "black")
        self.chess_color = chess_color
        self.set_background_color()

    def set_background_color(self):
        if self.chess_color == "white":
            self.background_color = Back.LIGHTWHITE_EX
        else:
            self.background_color = ""

    def add_piece(self, p):
        self.piece = p

    def get_piece(self):
        return self.piece

    def remove_piece(self):
        self.piece = None

    def check_if_free(self):
        if self.piece is None:
            return True
        return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        ret = ""
        ret += self.background_color
        if self.piece is None:
            ret += "   "
        else:
            if self.piece.color == "white":
                ret += Style.BRIGHT + Fore.BLUE
            else:
                ret += Style.DIM + Fore.RED
            ret += f" {self.piece.symbol} "
        ret += Style.RESET_ALL
        return ret


if __name__ == "__main__":
    pass
