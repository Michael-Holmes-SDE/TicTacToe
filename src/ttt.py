#!/usr/bin/python3

#                         ,
#                        (o)<  DuckieCorp Software License
#                   .____//
#                    \ <' )   Copyright (c) 2023 Erik Falor
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
#
# You may reproduce and distribute copies of the Work in any medium,
# with or without modifications, provided that You meet the following
# conditions:
#
#   (a) You must give any other recipients of the Work a copy of this
#       License; and
#   (b) You must cause any modified files to carry prominent notices
#       stating that You changed the files; and
#   (c) You must retain, in the Source form of the files that You
#       distribute, all copyright, patent, trademark, and attribution
#       notices from the Source form of the Work; and
#   (d) You do not misuse the trade names, trademarks, service marks,
#       or product names of the Licensor, except as required for
#       reasonable and customary use of the source files.

#    ___   ____  ______
#   / _ | /  _/ /_  __/__ ___ ___ _
#  / __ |_/ /    / / / -_) _ `/  ' \
# /_/ |_/___/   /_/  \__/\_,_/_/_/_/

from time import sleep
from board import *
from graphics import *
from strategy import *
CPU_DELAY = 0.75


def player_select():
    while True:
        print("0)", red("X"),   cyan("CPU  "), "vs.", green("O"), cyan("CPU"))
        print("1)", red("X"), yellow("Human"), "vs.", green("O"), cyan("CPU"))
        print("2)", red("X"),   cyan("CPU  "), "vs.", green("O"), yellow("Human"))
        print("3)", red("X"), yellow("Human"), "vs.", green("O"), yellow("Human"))
        p = input("Choose game mode [0-3] or Q to quit > ")
        if p == "0" or p == "1" or p == "2" or p == "3":
            return int(p)
        elif p.lower() == "joshua":
            return 4
        elif p.lower().startswith('q'):
            return p
        else:
            print("\nInvalid selection!\n")


def winner(board):
    """  	  	  
    Returns the winner of the game (if any), or False when there is no winner  	  	  
    """
    return horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)


def human_turn(board, letter):
    """  	  	  
    Return False if the game is over,  	  	  
           True to keep playing  	  	  
    """
    while True:
        choice = get_human_move(board, letter)
        if not choice:
            return False
        new_board = place(board, choice, letter)
        if not new_board:
            if letter == 'X':
                print(red("You can't play at {}!".format(choice)))
            else:
                print(green("You can't play at {}!".format(choice)))
        else:
            return new_board


def cpu_turn(board, letter, strategy, verbose=True):
    if letter == "X":
        color = red
    else:
        color = green
    if verbose:
        print(color("CPU {} is taking its turn...".format(letter)), end=' ', flush=True)
    sleep(CPU_DELAY)
    choice = strategy(board)
    if verbose:
        print(color("playing on {}\n".format(choice)))
    return place(board, choice, letter)


def keep_playing(board):
    """  	  	  
    Accepts a board or False as input  	  	  
           board: take another turn  	  	  
           False: the user has requested to quit the game  	  	  
    Return False if the game is over for any reason (quitting, win, lose or draw),  	  	  
           or a new board to keep playing  	  	  
    """
    if not board:
        return False
    who = winner(board)
    if who == "X":
        print(red("\n{} is the winner!\n".format(who)))
        return False
    elif who == "O":
        print(green("\n{} is the winner!\n".format(who)))
        return False
    elif full(board):
        print(yellow("\nStalemate.\n"))
        return False
    else:
        return board


def cpu_vs_cpu(strategy_x, strategy_o):
    """Game mode 0: run the game between two CPU opponents"""
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', strategy_x)
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', strategy_o)
        if not keep_playing(board):
            break
    show(board)


def cpu_vs_human(cpu_strategy):
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', cpu_strategy)
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_human():
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_cpu(cpu_strategy):
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', cpu_strategy)
        if not keep_playing(board):
            break
    show(board)


def game(strategy_x, strategy_o):
    global CPU_DELAY
    clear()
    print(cyan("GREETINGS PROFESSOR FALKEN\n"))
    sleep(CPU_DELAY)
    print(cyan("SHALL WE PLAY A GAME?\n"))
    sleep(CPU_DELAY * 2)
    orig_delay = CPU_DELAY
    clear()
    for _ in range(40):
        board = make_board()
        clear()
        while True:
            if CPU_DELAY > 0.025:
                CPU_DELAY *= 0.95
            home()
            show(board)
            board = cpu_turn(board, 'X', strategy_x, verbose=False)
            if not keep_playing(board):
                break
            home()
            show(board)
            board = cpu_turn(board, 'O', strategy_o, verbose=False)
            if not keep_playing(board):
                break
        clear()
        show(board)
        keep_playing(board)
        sleep(CPU_DELAY)
    CPU_DELAY = orig_delay
    sleep(CPU_DELAY)
    print(cyan("A STRANGE GAME.\n"))
    sleep(CPU_DELAY * 2)
    print(cyan("THE ONLY WINNING MOVE IS NOT TO PLAY.\n"))
    sleep(CPU_DELAY * 2)
    print(cyan("HOW ABOUT A NICE GAME OF CHESS?\n"))
    sleep(CPU_DELAY * 5)


if __name__ == '__main__':
    while True:
        logo()
        mode = player_select()
        if mode == 0:
            cpu_vs_cpu(strategy_oracle, strategy_oracle)
        elif mode == 1:
            human_vs_cpu(strategy_oracle)
        elif mode == 2:
            cpu_vs_human(strategy_oracle)
        elif mode == 3:
            human_vs_human()
        elif mode == 4:
            game(strategy_oracle, strategy_oracle)
        else:
            break
    print("Thanks for playing!")

