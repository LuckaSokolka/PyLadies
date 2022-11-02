from random import randrange
import time

# TICK-TACK-TOE


def score(area):  # function get list(area) and return result in accordance with area

    # draw
    if '-' not in area:
        print('"!"')
        quit()
    # players won
    elif (3 * player_symbol) in area:
        print('"X"')
        quit()
    # pc won
    elif (3 * pc_symbol) in area:
        print('"O"')
        quit()
    # next play
    else:
        print('"-"')


def move(area, position, symbol):  # put symbol into area, get area, position 1 - 19, symbol

    area = list(area)
    area[position] = symbol
    area = ''.join(area)
    return area

def kontrola(position):
    position = str(position)
    while position.isdigit():
      return position
    print("zadej číslo")


def player_move(area):  # get input(position) from player, test input and return area with symbol

    while True:
        position = int(input(f'Políčko (1 - {len(area)}): '))
        position = position - 1
        kontrola(position)
        while int(position) >= 0 and (int(position) < len(area)):
            if area[int(position)] != "-":
                print("políčko je obsazené")
                break
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
        print()
        play_area = pc_move(play_area)
        time.sleep(1)
        print(play_area, "pc")
        score(play_area)


pc_symbol = "O"
player_symbol = "X"
play_area = 20 * "-"
tick_tack_toe_1D(play_area)
