import time
from ai import pc_move, move


def player_move(area):
    # get input(position) from player, test input and return area with symbol

    while True:
        position = input('Políčko (1 - 20): ')
        if not position.isdigit():
            print("bereme jen číslo větší než 0")
            continue
        position = int(position) - 1
        if position > (len(area)):
            print("políčko je nedostupné")
            continue
        if (area[position] != "-"):
            print("obsazeno")
            continue
        return move(area, position, player_symbol)


def score(area):
    # function get list(area) and return result in accordance with area
    if (3 * player_symbol) in area:
        return player_symbol
    elif (3 * pc_symbol) in area:
        return pc_symbol
    elif '-' not in area:
        return 0
    else:
        return "-"


def tick_tack_toe_test(play_area):  # all together in game

    while True:
        play_area = player_move(play_area)
        print(play_area, "hráč")
        score(play_area)
        if score(play_area) != "-":
            break
        play_area = pc_move(play_area)
        time.sleep(1)
        print(play_area, "pc")
        score(play_area)
        if score(play_area) != "-":
            break

    if score(play_area) == player_symbol:
        print("Vyhral hráč")
    elif score(play_area) == pc_symbol:
        print("Vyhral pc")
    else:
        print("Remíza")


player_symbol = "X"
pc_symbol = "O"
