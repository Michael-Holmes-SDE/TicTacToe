#from boardUiTeam import *  # Change to boardUiTeam to test that module
#from strategy import *  # This statement SHOULD be unnecessary
#from model import *


def logo():  	  	  
    """Display the game's colorful logo"""  	  	  
    print()  	  	  
    print(red('888888888               '), yellow('888888888                '), green('888888888                 '))  	  	  
    print(red('"8888888" ooooo  ooooo  '), yellow('"8888888" ooo     ooooo  '), green('"8888888"  ooo    ooooo   '))  	  	  
    print(red('   888     888  88   8  '), yellow('   888    888    88   8  '), green('   888   88   88  8       '))  	  	  
    print(red('   888     888  88      '), yellow('   888   8ooo8   88      '), green('   888   88   88  8ooooo  '))  	  	  
    print(red('   888     888  88    88'), yellow('   888  888  888 88    88'), green('   888   88o  88 o88      '))  	  	  
    print(red('   888    88888  888888"'), yellow('   888  888  888  888888"'), green('   888   "888888 888888888'))  	  	  
    print("                                                            ", "by ", yellow("DuckieCorp"), "(tm)", sep='')  	  	  
    print(cyan("\nWOULD YOU LIKE TO PLAY A GAME?\n"))  	  	  


def show(board):  	  	  
    """  	  	  
    Display the Tic-Tac-Toe board on the screen, in color  	  	  

    When the optional parameter 'clear' is True, clear the screen before printing the board  	  	  
    """  	  	  
    if board:  	  	  
        print(" {} | {} | {}\n---+---+---\n {} | {} | {}\n---+---+---\n {} | {} | {}\n".format(  	  	  
            color(board[0][0]), color(board[0][1]), color(board[0][2]),  	  	  
            color(board[1][0]), color(board[1][1]), color(board[1][2]),  	  	  
            color(board[2][0]), color(board[2][1]), color(board[2][2])))  	  	  


def black(s):  	  	  
    return "\x1b[1;30m{}\x1b[0m".format(s)  	  	  


def red(s):  	  	  
    return "\x1b[1;31m{}\x1b[0m".format(s)  	  	  


def green(s):  	  	  
    return "\x1b[1;32m{}\x1b[0m".format(s)  	  	  


def yellow(s):  	  	  
    return "\x1b[1;33m{}\x1b[0m".format(s)  	  	  


def blue(s):  	  	  
    return "\x1b[1;34m{}\x1b[0m".format(s)  	  	  


def magenta(s):  	  	  
    return "\x1b[1;35m{}\x1b[0m".format(s)  	  	  


def cyan(s):  	  	  
    return "\x1b[1;36m{}\x1b[0m".format(s)  	  	  


def white(s):  	  	  
    return "\x1b[1;37m{}\x1b[0m".format(s)  	  	  


def color(s):  	  	  
    if s == 'X':  	  	  
        return red(s)  	  	  
    elif s == 'O':  	  	  
        return green(s)  	  	  
    else:  	  	  
        return yellow(s)  	  	  


def home():  	  	  
    """return cursor to home position (upper left corner)"""  	  	  
    print(end="\x1b[H")  	  	  


def clear():  	  	  
    """clear the screen and return cursor to home position"""  	  	  
    print(end="\x1b[H\x1b[J", flush=True)  	  	  
