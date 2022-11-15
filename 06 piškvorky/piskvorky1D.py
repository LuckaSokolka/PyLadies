from random import randrange
import time

# TICK-TACK-TOE


def score(area):
    # function get list(area) and return result in accordance with area

    # draw
    if '-' not in area:
        print('"!" REMÍZA')
    # players won
    elif (3 * player_symbol) in area:
        print('"X" VYHRÁL')
    # pc won
    elif (3 * pc_symbol) in area:
        print('"O VYHRÁL"')
    # next play
    else:
        print('"-"')


def move(area, position, symbol):
    # put symbol into area, get area, position 1 - 19, symbol

    area = list(area)
    area[position] = symbol
    area = ''.join(area)
    return area


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


def pc_move(area):  # move for pc, position choose by randrange

    while True:
        position = randrange(1, 20)
        if area[int(position)] == "-":
            return move(area, position, pc_symbol)


def tick_tack_toe_1D(play_area):  # all together in game

    while True:
        play_area = player_move(play_area)
        print(play_area, "hráč")
        score(play_area)
        if ((3 * player_symbol) in play_area):
            break
        play_area = pc_move(play_area)
        time.sleep(1)
        print(play_area, "pc")
        score(play_area)
        if ((3 * pc_symbol) in play_area):
            break


pc_symbol = "O"
player_symbol = "X"
play_area = 20 * "-"
tick_tack_toe_1D(play_area)
