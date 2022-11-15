from piskvorky import move, score
from ai import pc_move


def test_move():
    symbol = 'X'
    play_area = "--------------------"
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


def test_score():
    area_test_player_win = ("XXX-----------------")
    area_test_pc_win = ("OOO-----------------")
    area_test_remiza = ("OXOXOXOXOXOXOXOXOXOX")
    area_test_else = ("OXOXOX--------------")
    assert score(area_test_player_win) == "X"
    assert score(area_test_pc_win) == "O"
    assert score(area_test_remiza) == 0
    assert score(area_test_else) == "-"
