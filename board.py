from tile import Tile
class Board:
    board = None

    def __init__(self):
        print("new board made")

    def create_board(self):
        self.board = []
        color = "white"
        for x in range(8):
            current = []
            for y in range(8):
                temp = Tile(x,y,color)
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

    def print_board(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                print(self.board[x][y],end ="")
            print()




if __name__ == "__main__":
    b = Board()
    b.create_board()