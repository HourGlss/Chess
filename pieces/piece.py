class Piece:
    color = None
    symbol = None

    def __init__(self, color):
        assert (color == "white" or color == "black")
        self.color = color

    def is_valid_move(self, board, startx, starty, endx, endy):
        # print("Called from Piece")
        return False

    def attempt_capture(self, board, theirx, theiry):
        possible_enemy = board.get_piece_at(theirx, theiry)
        if possible_enemy is None:
            return False
        if self.color != possible_enemy.color:
            return True
        return False

    def forms_x(self, startx, starty, endx, endy):
        for i in range(-7, 8, 1):
            if startx + i == endx and starty + i == endy:
                return True
            elif startx - i == endx and starty - i == endy:
                return True
            elif startx - i == endx and starty + i == endy:
                return True
            elif startx + i == endx and starty - i == endy:
                return True
        return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.symbol
