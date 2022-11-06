# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    ship_info = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}

    p1 = [["-" for i in range(board_size)] for j in range(board_size)]
    p2 = [["-" for i in range(board_size)] for j in range(board_size)]
    p2_in_p1_turn = [["-" for i in range(board_size)] for j in range(board_size)]
    p1_in_p2_turn = [["-" for i in range(board_size)] for j in range(board_size)]
    lst = [p1, p2]
    lst_p1_turn = [p1, p2_in_p1_turn]
    lst_p2_turn = [p1_in_p2_turn, p2]
    p1_confirmation = " "
    p2_confirmation = " "

    p1ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    p1used = []
    p2ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    p2used = []
    print_3d_list(lst)

    while len(
            p1ships) != 0:  # This code block repeats until there are no ships left so the game can skip to next phase.
        occupied_sign = False

        print_ships_to_be_placed()

        for ship in p1ships:  # This code block prints the remaining ships for the player.
            print_single_element(ship)
        print_empty_line()

        print_player_turn_to_place(1)
        print_to_place_ships()

        placement = input()  # This code block takes the input and creates a list for the placement information.
        placement = placement.lower()
        placement = placement.strip()
        placement_lst = placement.split()

        # The block below checks if the input has a proper format. If not, returns to the beginning.
        if len(placement_lst) < 4 or placement_lst[1].isdigit() == False or placement_lst[2].isdigit() == False:
            try:
                int(placement_lst[1])
                int(placement_lst[2])
                print_incorrect_coordinates()
                print_3d_list(lst_p1_turn)
                continue
            except:
                print_incorrect_input_format()
                print_3d_list(lst_p1_turn)
                continue

        # The block below checks whether the coordinates are in the board. If not, returns to the beginning.
        if 1 > int(placement_lst[1]) or 10 < int(placement_lst[1]) or 1 > int(placement_lst[2]) or 10 < int(
                placement_lst[2]):
            print_incorrect_coordinates()
            print_3d_list(lst_p1_turn)
            continue

        # The block below checks if the ship name in the input is valid. If not, returns to the beginning.
        if placement_lst[0] not in ship_info:
            print_incorrect_ship_name()
            print_3d_list(lst_p1_turn)
            continue

        # The block below checks if the orientation is valid. If not, returns to the beginning.
        if placement_lst[3].lower() not in ("h", "v"):
            print_incorrect_orientation()
            print_3d_list(lst_p1_turn)
            continue

        # The block below checks if the ship is already used. If so, returns to the beginning.
        if placement_lst[0] in p1used:
            print_ship_is_already_placed(placement_lst[0].capitalize())
            print_3d_list(lst_p1_turn)
            continue




        elif placement_lst[0] in ship_info:
            if placement_lst[3].lower() == "h":

                # The block below checks whether the ship fits to the board with the given input.
                # If not, returns to the beginning.
                if int(placement_lst[1]) - 1 + ship_info[placement_lst[0]] > 10:
                    print_ship_cannot_be_placed_outside(placement_lst[0].capitalize())
                    print_3d_list(lst_p1_turn)
                    continue

                # The block below checks whether the ship intersects with an already placed one.
                # If so, returns to the beginning.
                for i in range(int(placement_lst[1]) - 1, int(placement_lst[1]) - 1 + ship_info[placement_lst[0]]):
                    if lst_p1_turn[0][int(placement_lst[2]) - 1][i] == "#":
                        occupied_sign = True

                if occupied_sign:
                    print_ship_cannot_be_placed_occupied(placement_lst[0].capitalize())
                    print_3d_list(lst_p1_turn)
                    continue

                # The block below places the ship.
                for i in range(int(placement_lst[1]) - 1, int(placement_lst[1]) - 1 + ship_info[placement_lst[0]]):
                    lst_p1_turn[0][int(placement_lst[2]) - 1][i] = "#"

            if placement_lst[3].lower() == "v":

                # The block below checks whether the ship fits to the board with the given input.
                # If not, returns to the beginning.
                if (int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]) > 10:
                    print_ship_cannot_be_placed_outside(placement_lst[0].capitalize())
                    print_3d_list(lst_p1_turn)
                    continue

                # The block below checks whether the ship intersects with an already placed one.
                # If so, returns to the beginning.
                for i in range(int(placement_lst[2]) - 1, int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]):
                    if lst_p1_turn[0][i][int(placement_lst[1]) - 1] == "#":
                        occupied_sign = True
                if occupied_sign:
                    print_ship_cannot_be_placed_occupied(placement_lst[0].capitalize())
                    print_3d_list(lst_p1_turn)
                    continue

                # The block below places the ship.
                for i in range(int(placement_lst[2]) - 1, int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]):
                    lst_p1_turn[0][i][int(placement_lst[1]) - 1] = "#"

            # The block below creates a list of already used ships so that they can be recognized.
            for used in p1ships:
                if used.lower() == placement_lst[0]:
                    p1ships.remove(used)
                    p1used.append(used.lower())

        print_3d_list(lst_p1_turn)

        # The block below takes a confirmation from the user. If it takes no, it resets the board and the ships.
        while len(p1ships) == 0 and p1_confirmation.lower() not in ("y", "n"):
            print_confirm_placement()
            p1_confirmation = input()
            if p1_confirmation.lower() == "n":
                for i in range(board_size):
                    for j in range(board_size):
                        lst_p1_turn[0][i][j]="-"


                p1ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                p1used.clear()
                p1_confirmation = " "
                print_3d_list(lst_p1_turn)

    print_3d_list(lst_p2_turn)
    while len(
            p2ships) != 0:  # This code block repeats until there are no ships left so the game can skip to next phase.
        occupied_sign = False

        print_ships_to_be_placed()

        for ship in p2ships:  # This code block prints the remaining ships for the player.
            print_single_element(ship)
        print_empty_line()

        print_player_turn_to_place(2)
        print_to_place_ships()

        placement = input()  # This code block takes the input and creates a list for the placement information.
        placement = placement.lower()
        placement = placement.strip()
        placement_lst = placement.split()

        # The block below checks if the input has a proper format. If not, returns to the beginning.
        if len(placement_lst) < 4 or placement_lst[1].isdigit() == False or placement_lst[2].isdigit() == False:
            try:
                int(placement_lst[1])
                int(placement_lst[2])
                print_incorrect_coordinates()
                print_3d_list(lst_p2_turn)
                continue
            except:
                print_incorrect_input_format()
                print_3d_list(lst_p2_turn)
                continue

        # The block below checks whether the coordinates are in the board. If not, returns to the beginning.
        if 1 > int(placement_lst[1]) or 10 < int(placement_lst[1]) or 1 > int(placement_lst[2]) or 10 < int(
                placement_lst[2]):
            print_incorrect_coordinates()
            print_3d_list(lst_p2_turn)
            continue

        # The block below checks if the ship name in the input is valid. If not, returns to the beginning.
        if placement_lst[0] not in ship_info:
            print_incorrect_ship_name()
            print_3d_list(lst_p2_turn)
            continue

        # The block below checks if the orientation is valid. If not, returns to the beginning.
        if placement_lst[3].lower() not in ("h", "v"):
            print_incorrect_orientation()
            print_3d_list(lst_p2_turn)
            continue

        # The block below checks if the ship is already used. If so, returns to the beginning.
        if placement_lst[0] in p2used:
            print_ship_is_already_placed(placement_lst[0].capitalize())
            print_3d_list(lst_p2_turn)
            continue




        elif placement_lst[0] in ship_info:
            if placement_lst[3].lower() == "h":

                # The block below checks whether the ship fits to the board with the given input.
                # If not, returns to the beginning.
                if int(placement_lst[1]) - 1 + ship_info[placement_lst[0]] > 10:
                    print_ship_cannot_be_placed_outside(placement_lst[0].capitalize())
                    print_3d_list(lst_p2_turn)
                    continue

                # The block below checks whether the ship intersects with an already placed one.
                # If so, returns to the beginning.
                for i in range(int(placement_lst[1]) - 1, int(placement_lst[1]) - 1 + ship_info[placement_lst[0]]):
                    if lst_p2_turn[1][int(placement_lst[2]) - 1][i] == "#":
                        occupied_sign = True

                if occupied_sign:
                    print_ship_cannot_be_placed_occupied(placement_lst[0].capitalize())
                    print_3d_list(lst_p2_turn)
                    continue

                # The block below places the ship.
                for i in range(int(placement_lst[1]) - 1, int(placement_lst[1]) - 1 + ship_info[placement_lst[0]]):
                    lst_p2_turn[1][int(placement_lst[2]) - 1][i] = "#"

            if placement_lst[3].lower() == "v":

                # The block below checks whether the ship fits to the board with the given input.
                # If not, returns to the beginning.
                if (int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]) > 10:
                    print_ship_cannot_be_placed_outside(placement_lst[0].capitalize())
                    print_3d_list(lst_p2_turn)
                    continue

                # The block below checks whether the ship intersects with an already placed one.
                # If so, returns to the beginning.
                for i in range(int(placement_lst[2]) - 1, int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]):
                    if lst_p2_turn[1][i][int(placement_lst[1]) - 1] == "#":
                        occupied_sign = True
                if occupied_sign:
                    print_ship_cannot_be_placed_occupied(placement_lst[0].capitalize())
                    print_3d_list(lst_p2_turn)
                    continue

                # The block below places the ship.
                for i in range(int(placement_lst[2]) - 1, int(placement_lst[2]) - 1 + ship_info[placement_lst[0]]):
                    lst_p2_turn[1][i][int(placement_lst[1]) - 1] = "#"

            # The block below creates a list of already used ships so that they can be recognized.
            for used in p2ships:
                if used.lower() == placement_lst[0]:
                    p2ships.remove(used)
                    p2used.append(used.lower())

        print_3d_list(lst_p2_turn)

        # The block below takes a confirmation from the user. If it takes no, it resets the board and the ships.
        while len(p2ships) == 0 and p2_confirmation.lower() not in ("y", "n"):
            print_confirm_placement()
            p2_confirmation = input()
            if p2_confirmation.lower() == "n":
                for i in range(board_size):
                    for j in range(board_size):
                        lst_p2_turn[1][i][j]="-"
                p2ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                p2used.clear()
                p2_confirmation = " "
                print_3d_list(lst_p2_turn)

    p1_hp = 17
    p2_hp = 17
    p1_hit = True
    p2_hit = True
    p1_yield = "done"
    p2_yield = "done"
    print_3d_list(lst_p1_turn)

    while p1_hp != 0 and p2_hp != 0:

        # The block below gets the input from p1, if it is p1's turn.
        if p1_hit:
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            shot = input()
            shot = shot.lower()
            shot = shot.strip()
            shot_lst = shot.split()

            # The block below checks if the input has a valid format. If not, returns to the beginning.
            if len(shot_lst) < 2 or shot_lst[0].isdigit() == False or shot_lst[1].isdigit() == False:
                try:
                    int(shot_lst[0])
                    int(shot_lst[1])
                    print_incorrect_coordinates()
                    print_3d_list(lst_p1_turn)
                    continue
                except:
                    print_incorrect_input_format()
                    print_3d_list(lst_p1_turn)
                    continue

            # The block below checks if the input indicates valid coordinates. If not, returns to the beginning.
            if int(shot_lst[0]) > 10 or int(shot_lst[0])<0 or  int(shot_lst[1]) > 10 or int(shot_lst[1])<0 :
                print_incorrect_coordinates()
                print_3d_list(lst_p1_turn)
                continue

            # The block below checks whether the tile is already hit. If so, returns to the beginning.
            if lst_p1_turn[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "O" or \
                    lst_p1_turn[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "!":
                print_tile_already_struck()
                print_3d_list(lst_p1_turn)
                continue

            # The block below checks whether the chosen coordinates contain a ship.
            # If so, marks it and returns to the beginning.
            if lst[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "#":
                lst[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "!"
                lst_p1_turn[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "!"
                print_hit()
                print_3d_list(lst_p1_turn)
                p2_hp -= 1
                p1_hit = True
                p2_hit = False
                continue

            # The block below checks whether the chosen coordinates contain a ship.
            # If not, marks it and returns to the beginning.
            if lst[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "-":
                lst[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "O"
                lst_p1_turn[1][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "O"
                p1_hit = False
                p2_hit = True
                p1_yield = " "
                print_miss()

            # The block below ends the turn after a miss.
            while p1_yield.lower() != "done":
                print_type_done_to_yield(2)
                p1_yield = input()
                if p1_yield.lower() == "done":
                    print_3d_list(lst_p2_turn)

        # The block below gets the input from p2, if it is p2's turn.
        if p2_hit:
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            shot = input()
            shot = shot.lower()
            shot = shot.strip()
            shot_lst = shot.split()

            # The block below checks if the input has a valid format. If not, returns to the beginning.
            if len(shot_lst) < 2 or shot_lst[0].isdigit() == False or shot_lst[1].isdigit() == False:
                try:
                    int(shot_lst[0])
                    int(shot_lst[1])
                    print_incorrect_coordinates()
                    print_3d_list(lst_p2_turn)
                    continue
                except:
                    print_incorrect_input_format()
                    print_3d_list(lst_p2_turn)
                    continue

            # The block below checks if the input indicates valid coordinates. If not, returns to the beginning.
            if int(shot_lst[0]) > 10 or int(shot_lst[0])<0 or  int(shot_lst[1]) > 10 or int(shot_lst[1])<0 :
                print_incorrect_coordinates()
                print_3d_list(lst_p2_turn)
                continue

            # The block below checks whether the tile is already hit. If so, returns to the beginning.
            if lst_p2_turn[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "O" or \
                    lst_p2_turn[0][int(shot_lst[1]) - 1][
                        int(shot_lst[0]) - 1] == "!":
                print_tile_already_struck()
                print_3d_list(lst_p2_turn)
                continue

            # The block below checks whether the chosen coordinates contain a ship.
            # If so, marks it and returns to the beginning
            if lst[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "#":
                lst[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "!"
                lst_p2_turn[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "!"
                print_hit()
                print_3d_list(lst_p2_turn)
                p1_hp -= 1
                p2_hit = True
                p1_hit = False
                continue

            # The block below checks whether the chosen coordinates contain a ship.
            # If not, marks it and returns to the beginning.
            if lst[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] == "-":
                lst[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "O"
                lst_p2_turn[0][int(shot_lst[1]) - 1][int(shot_lst[0]) - 1] = "O"
                p2_hit = False
                p1_hit = True
                p2_yield = " "
                print_miss()

            # The block below ends the turn after a miss.
            while p2_yield.lower() != "done":
                print_type_done_to_yield(1)
                p2_yield = input()
                if p2_yield.lower() == "done":
                    print_3d_list(lst_p1_turn)

    # The block below checks who finished the enemy ships first. Then, prints a proper win message.
    if p2_hp == 0:
        print_player_won(1)
        print_thanks_for_playing()
    if p1_hp == 0:
        print_player_won(2)
        print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()
