from piskvorky import move
from ai import pc_move
from random import randrange


def test_move():
    symbol = 'X'
    assert move(20 * "-", 19, symbol) == "-------------------X"
    assert move(20 * "-", 0, symbol) == "X-------------------"


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


def test_score():
    area_remiza = ("XOXOXOXOXOXOXOXOXOXO")
    assert '-' not in area_remiza
    area_player_win = ("XXX-----------------")
    assert (3 * "X") in area_player_win
    area_pc_win = ("------OOO-----------")
    assert (3 * "O") in area_pc_win
    area_next_game = ("XOXXO-----XO----OX--")
    assert "-" in area_next_game


def player_move_without_input(area, position):

    while True:
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
        return move(area, position, "X")


def test_player_move():
    area_player = player_move_without_input("---O----------XX-O--", "2")
    assert len(area_player) == 20
    assert area_player.count('O') == 2
    assert area_player.count('-') == 15
    assert area_player.count('X') == 3