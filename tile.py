import colorama
from colorama import Fore, Back, Style


class Tile:
    x = None
    y = None
    piece = None
    color = None

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        assert (color == "white" or color == "black")
        self.color = color

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
        if self.color == "white":
            ret += Back.LIGHTWHITE_EX
        else:
            ret += ""
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
