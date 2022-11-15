from random import randrange


def pc_move(area):  # move for pc, position choose by randrange

    while True:
        position = randrange(0, 19)
        if area[int(position)] == "-":
            return move(area, position, pc_symbol)


def move(area, position, symbol):
    # put symbol into area, get area, position 1 - 19, symbol

    area = list(area)
    area[position] = symbol
    area = ''.join(area)
    return area


pc_symbol = "O"
