from piskvorky import move
from ai import pc_move
import time


player_symbol = "X"
pc_symbol = "O"
play_area = 20 * "-"


def test_move():
    symbol = 'X'
    assert move(play_area, 19, symbol) == "-------------------X"
    assert move(play_area, 0, symbol) == "X-------------------"


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


def test_score():
    area_test_player_win = ("XXX-----------------")
    area_test_pc_win = ("OOO-----------------")
    area_test_remiza = ("OXOXOXOXOXOXOXOXOXOX")
    area_test_else = ("OXOXOX--------------")
    assert score(area_test_player_win) == "X"
    assert score(area_test_pc_win) == "O"
    assert score(area_test_remiza) == 0
    assert score(area_test_else) == "-"
