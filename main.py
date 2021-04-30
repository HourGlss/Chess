from board import Board
import colorama
import sys
from config import Config
import socket
import ast

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


def main(server=True,ip=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    colorama.init()
    b = Board()
    b.create_board()
    b.reset_pieces()
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
    # b.custom_piece_placement()
    print_on_next = True
    selected = False
    parsed_user_input = None
    msg = ""
    if server:
        print("Waiting for a connection")
        connection, client_address = sock.accept()
        print(f"Connection found from: {client_address}")
    while True:
        if print_on_next:
            clear_screen()
            msg = f"{current_player}'s turn"
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

                            if not b.move_piece(player,parsed_user_input):
                                print_on_next = False
                            else:
                                # THIS WAS A WORKING MOVE
                                if server:
                                    connection.send(str(parsed_user_input).encode())
                                    print(f"server SENT {parsed_user_input}")
                                else:
                                    sock.send(str(parsed_user_input).encode())
                                    print(f"client SENT {parsed_user_input}")
                                print_on_next = True
                                if current_player == "white":
                                    current_player = "black"
                                else:
                                    current_player = "white"

                        elif len(parsed_user_input) == 2:
                            selected = True

                else:
                    parsed_user_input = parse_command(user_input[4:])
                    b.show_if_tile_under_attack(parsed_user_input[0],parsed_user_input[1])
                    print_on_next = False
            else:
                break
        else:
            if server:
                data = connection.recv(4096)
                remote_user_input = ast.literal_eval(data.decode())
                print(f"server received: {remote_user_input}")
                b.move_piece("black",remote_user_input)
                print_on_next = True
                if current_player == "white":
                    current_player = "black"
                else:
                    current_player = "white"
            if not server:
                data = sock.recv(4096)
                remote_user_input = ast.literal_eval(data.decode())
                print(f"client received: {remote_user_input}")
                b.move_piece("white", remote_user_input)
                print_on_next = True
                if current_player == "white":
                    current_player = "black"
                else:
                    current_player = "white"




def clear_screen():
    # ONE OF THESE WORKS
    colorama.ansi.clear_screen()
    sys.stdout.write('\u001b[2J')


if __name__ == "__main__":
    done = False
    while not done:
        choice = str(input("Do you want to host and be white Y/N\n").lower())
        if choice == "y":
            done = True
            main()
        elif choice == "n":
            ip_to_connect_to = str(input("What is the server's ip?\n"))

            main(server=False, ip=ip_to_connect_to)
            done = True
