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


player_symbol = "X"
pc_symbol = "O"
