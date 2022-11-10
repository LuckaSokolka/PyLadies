from random import randrange
from piskvorky import move


def pc_move(area):  # move for pc, position choose by randrange

    while True:
        position = randrange(0, 19)
        if area[int(position)] == "-":
            return move(area, position, pc_symbol)


pc_symbol = "O"
