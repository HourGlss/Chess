class Config:
    BOARD_SIZE = 8
    ranks = range(BOARD_SIZE, 0, -1)
    files = [chr(e) for e in range(ord('a'), ord('a') + BOARD_SIZE)]