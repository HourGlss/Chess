from board import Board
import colorama
import sys
from config import Config
import socket
import ast
import sys

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


def transpose_x_y_to_rank_file(x, y):
    return [chr(e) for e in range(97, 97 + 26)][x], Config.BOARD_SIZE - y


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


def main(server=True, ip=None, no_network=False):
    moves_made = []

    colorama.init()
    b = Board()
    b.create_board()
    # b.reset_pieces()
    b.custom_piece_placement()
    current_player = None
    player = None
    if not no_network:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = None
        if server:
            server_address = ('0.0.0.0', 4501)
            sock.bind(server_address)
            sock.listen(1)
            player = "white"
            current_player = "white"
        if not server:
            player = "black"
            current_player = "white"
            server_address = (ip, 4501)
        sock.connect(server_address)
    else:
        player = "white"
        current_player = "white"
    # b.custom_piece_placement()
    print_on_next = True
    selected = False
    parsed_user_input = None
    msg = ""
    last_move = ""

    if server and not no_network:
        print("Waiting for a connection")
        connection, client_address = sock.accept()
        print(f"Connection found from: {client_address}")
    while True:
        if print_on_next:
            # clear_screen()
            msg = f"{current_player}'s turn {last_move}"
            print(msg)
            b.print_board(selected=selected, parsed_user_input=parsed_user_input)
            selected = False
        if player == current_player:
            user_input = input("Select or FROM TO or Q or ATK\n").lower()

            if user_input != "q":
                if not user_input.startswith("atk"):
                    parsed_user_input = parse_command(user_input)
                    if parsed_user_input is not None:
                        if len(parsed_user_input) == 4:
                            # CHECK FOR CHECK BEFORE MOVEMENT
                            in_check = b.check_for_check(current_player)
                            piece_moved = b.move_piece(player, parsed_user_input)
                            still_in_check = b.check_for_check(current_player)
                            if in_check and still_in_check:
                                b.move_piece(player,)
                            if not piece_moved[0]:
                                print_on_next = False
                            else:


                                # THIS WAS A WORKING MOVE
                                if not no_network:
                                    if server:
                                        connection.send(str(parsed_user_input).encode())
                                        # print(f"server SENT {parsed_user_input}")
                                        # last_move = parsed_user_input
                                    elif not server:
                                        sock.send(str(parsed_user_input).encode())
                                        # print(f"client SENT {parsed_user_input}")
                                        # last_move = parsed_user_input
                                print_on_next = True
                                if current_player == "white":
                                    current_player = "black"
                                    if no_network:
                                        player ="black"
                                else:
                                    current_player = "white"
                                    if no_network:
                                        player = "white"

                        elif len(parsed_user_input) == 2:
                            selected = True

                else:
                    parsed_user_input = parse_command(user_input[4:])
                    b.show_if_tile_under_attack(parsed_user_input[0], parsed_user_input[1])
                    print_on_next = False
            else:
                break
        else:
            if not no_network:
                if server:
                    data = connection.recv(4096)
                    remote_user_input = ast.literal_eval(data.decode())
                    # print(f"server received: {remote_user_input}")
                    piece_moved = b.move_piece("black", remote_user_input)
                    print_on_next = True
                    if current_player == "white":
                        current_player = "black"
                    else:
                        current_player = "white"
                if not server:
                    data = sock.recv(4096)
                    remote_user_input = ast.literal_eval(data.decode())
                    print(f"client received: {remote_user_input}")
                    piece_moved = b.move_piece("white", remote_user_input)
                    print_on_next = True
                    if current_player == "white":
                        current_player = "black"
                    else:
                        current_player = "white"
            if not no_network:
                last_move = f"{piece_moved[1].__class__.__name__} moved to {transpose_x_y_to_rank_file(remote_user_input[2], remote_user_input[3])[0]}{transpose_x_y_to_rank_file(remote_user_input[2], remote_user_input[3])[1]}"


def clear_screen():
    # ONE OF THESE WORKS
    colorama.ansi.clear_screen()
    sys.stdout.write('\u001b[2J')


if __name__ == "__main__":
    done = False
    while not done:
        choice = str(input("Do you want to host and be white Y/N/L (L FOR LOCAL)\n").lower())
        if choice == "y":
            done = True
            main()
        elif choice == "n":
            ip_to_connect_to = str(input("What is the server's ip?\n"))

            main(server=False, ip=ip_to_connect_to)
            done = True

        elif choice == 'l':
            main(no_network=True)
            done = True
