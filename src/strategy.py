import random
from board import first_open_cell
from board import open_cells
from model import *
from ttt import *


def strategy_dumb(b):
    """Picks the first open square

    If it happens that NO squares are left, this function returns None, by default.
    However, that should never happen.  In a "real" game at least one square is
    always open, and the return statement will ALWAYS be reached.
    """
    return first_open_cell(b)


def strategy_random(b):
    """Picks an open square at random

    If it happens that NO squares are left, this function will raise IndexError.
    However, that should never happen.  In a "real" game at least one square is
    always open.
    """
    return random.choice(open_cells(b))


def strategy_oracle(b):
    """  	  	  
    CPU picks the optimal move by consulting a ML-trained model.  Technically  	  	  
    it's just a lookup table, but it was made with a program, so it was  	  	  
    basically "learned" by a machine.  	  	  

    For variety's sake, X's first play is chosen at random.  	  	  

    Otherwise, the current board state is searched for in MODEL, which is a  	  	  
    tuple of 9 sub-tables.  When a matching state is found, the index # of the  	  	  
    sub-table indicates which move to take.  	  	  

    Example: suppose the current game board looks like this:  	  	  
        ('O', 2, 3, 'O', 5, 'X', 7, 'X', 'X')  	  	  

    There are 3 X's and two O's; it is O's turn.  This same board is found  	  	  
    under sub-table 6 of MODEL.  This means that 'O' should mark square 7 of  	  	  
    the game board (adding 1 because Python tuples start at 0).  	  	  

    Every possible game state is found in MODEL.  I am 99% positive that is  	  	  
    impossible to reach the final `return False` statement at the end of the  	  	  
    function.  	  	  
    """
    findx = False
    for i in b:
        for j in i:
            if j == "X":
                findx = True
                break
    if not findx:
        return random.choice(open_cells(b))

    oneDimensionB = []
    for k in b:
        for l in k:
            oneDimensionB.append(l)
    for i in range(len(MODEL)):
        for j in range(len(MODEL[i])):
            if tuple(oneDimensionB) == MODEL[i][j]:
                del oneDimensionB
                return int(i + 1)
