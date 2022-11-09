from piskvorky import move, player_move
from ai import pc_move
from random import randrange
import time


player_symbol = "X"
pc_symbol = "O"

def test_move():
    symbol = 'X'
    pole = 20 * "-"
    assert move(pole, 19, symbol) == "-------------------X"
    assert move(pole, 0, symbol) == "X-------------------"


def test_pc_move():
    area_test = pc_move(20 * "-")
    area_test_next = pc_move("--X-----------O-----")
    assert len(area_test) == 20
    assert area_test.count('O') == 1
    assert area_test.count('-') == 19
    assert len(area_test_next) == 20
    assert area_test_next.count('O') == 2
    assert area_test_next.count('-') == 17
    assert area_test_next.count('X') == 1


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

def tick_tack_toe_1D(play_area):  # all together in game

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
