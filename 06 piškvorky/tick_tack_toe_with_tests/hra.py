import time
from piskvorky import player_move, score
from ai import pc_move


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
