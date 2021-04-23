from board import Board
import colorama
import sys
from config import Config


def transpose_rank_file_to_x_y(s):
    s = str(s).lower()
    file = s[0]
    rank = int(s[1])
    try:
        x = Config.files.index(file)
        y = Config.ranks.index(rank)
    except:
        return None
    return x, y


def parse_command(s):
    portions = s.split(" ")
    if len(portions) == 2:
        try:
            from_location, to_location = portions
        except:
            return None
        try:
            startx, starty = transpose_rank_file_to_x_y(from_location)
            endx, endy = transpose_rank_file_to_x_y(to_location)
        except:
            return None
        return startx, starty, endx, endy
    elif len(portions) == 1:
        try:
            startx, starty = transpose_rank_file_to_x_y(portions[0])
        except:
            return None
        return startx, starty


def main():
    colorama.init()
    b = Board()
    b.create_board()
    b.reset_pieces()
    # b.custom_piece_placement()
    player = "white"
    print_on_next = True
    selected = False
    parsed_user_input = None
    while True:
        if print_on_next:
            clear_screen()
            b.print_board(selected=selected, parsed_user_input=parsed_user_input)
            selected = False
        user_input = input("Select or FROM TO or Q\n").lower()

        if user_input != "q":
            parsed_user_input = parse_command(user_input)
            if parsed_user_input is not None:
                if len(parsed_user_input) == 4:

                    if not b.move_piece(player,parsed_user_input):
                        print_on_next = False
                        continue
                    else:
                        print_on_next = True
                        if player == "white":
                            player = "black"
                        else:
                            player = "white"
                elif len(parsed_user_input) == 2:
                    selected = True
                    continue

        else:
            break


def clear_screen():
    # ONE OF THESE WORKS
    colorama.ansi.clear_screen()
    sys.stdout.write('\u001b[2J')


if __name__ == "__main__":
    main()
