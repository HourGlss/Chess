from tile import Tile

# Import all the pieces
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class Board:
    board = None
    BOARD_SIZE = 8
    ranks = range(BOARD_SIZE, 0, -1)
    files = [chr(e) for e in range(ord('a'), ord('a') + BOARD_SIZE)]

    def __init__(self):
        pass

    def create_board(self):
        self.board = []
        color = "white"
        for x in range(self.BOARD_SIZE):
            current = []
            for y in range(self.BOARD_SIZE):
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
        for i in range(self.BOARD_SIZE):
            p = Pawn(color)
            self.board[i][6].add_piece(p)
        # Other white pieces
        pieces = [Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color),
                  Rook(color)]
        for i in range(self.BOARD_SIZE):
            self.board[i][7].add_piece(pieces[i])

        # BLACK PAWNS
        color = "black"
        for i in range(self.BOARD_SIZE):
            p = Pawn(color)
            self.board[i][1].add_piece(p)
        # Other black pieces
        pieces = [
            Rook(color), Knight(color), Bishop(color), Queen(color), King(color), Bishop(color), Knight(color),
                  Rook(color)]
        for i in range(self.BOARD_SIZE):
            self.board[i][0].add_piece(pieces[i])

    def print_board(self):
        y = 0
        for rank in self.ranks:
            print(f"{rank:2}", end="\t")
            x = 0
            for file in self.files:
                print(self.board[x][y], end="")
                x += 1
            y += 1
            print()
        print("\t", end="")
        for file in self.files:
            print(f" {file} ", end="")
        print()

    def __transpose_rank_file_to_x_y(self,s):
        s = str(s).lower()
        file = s[0]
        rank = int(s[1])
        try:
            x = self.files.index(file)
            y = self.ranks.index(rank)
        except:
            return None
        return x,y


    def __parse_command(self, s):
        portions = s.split(" ")
        try:
            from_location, to_location = portions
        except:
            return None
        try:
            startx,starty =  self.__transpose_rank_file_to_x_y(from_location)
            endx,endy = self.__transpose_rank_file_to_x_y(to_location)
        except:
            return None
        return startx,starty,endx,endy

    def move_piece(self, s):
        ret =  self.__parse_command(s)
        if ret is not None:
            startx, starty, endx, endy = ret
        else:
            print("Bad input!")
            return False
        # print(f"({startx},{starty}) -> ({endx},{endy})")
        piece = self.board[startx][starty].get_piece()
        if piece is not None:
            if piece.is_valid_move(self.board,startx,starty,endx,endy):
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
