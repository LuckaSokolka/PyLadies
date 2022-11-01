from random import randrange
import time

# TICK-TACK-TOE


def score(area):  # fce get list(area) and return result in accordance with area

    # draw
    if '-' not in area:
        print(' "!" ')
        quit()
    # players won
    elif (3 * player_symbol) in area:
        print(' "X" ')
        quit()
    # pc won
    elif (3 * pc_symbol) in area:
        print('"O"')
        quit()
    # next play
    else:
        print('"-"')
        quit()


def move(area, position, symbol):  # put symbol into area, get area, position 1 - 19, symbol

    area = list(area)
    area[position - 1] = symbol
    area = ''.join(area)
    return area


def player_move(area):  # get input(position) from player, test input and return area with symbol

    position = input('Kam umístit X? Vyber políčko 1 - 20. Tvá volba: ')
    while True:

        position = str(position)
        if position.isalpha():
            position = int(input("Políčko vybírej jen pomocí celých, kladných čísel. Políčko: "))
        position = int(position)

        while position <= 0 or position >= (len(area)+1):
            position = (int(input(f"Fungují jen celá, kladná čísla v rozmezí 1-{len(area)}. Políčko: ")))

        if (area[(int(position))-1] != player_symbol
                and area[(int(position))-1] != pc_symbol):
            return move(area, position, player_symbol)

        position = int(input("Políčko je obsazené, vyber jiné... "))


def pc_move(area):  # move for pc, position choose by randrange

    while True:
        position = randrange(1, 20)
        if (area[(int(position))-1] != pc_symbol
                and area[(int(position))-1] != player_symbol):
            return move(area, position, pc_symbol)


def tick_tack_toe_1D(play_area):  # all together in game

    while True:
        play_area = player_move(play_area)
        print(play_area, "hráč")
        play_area = pc_move(play_area)
        time.sleep(2)
        print(play_area, "pc")
        print(score(play_area))


pc_symbol = "O"
player_symbol = "X"
play_area = 20 * "-"
tick_tack_toe_1D(play_area)
