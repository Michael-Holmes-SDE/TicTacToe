from graphics import *


# FROM AI TEAM
def open_cells(b):
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    cs = []
    for i in b:
        for j in i:
            if type(j) is int:
                cs.append(j)
    return tuple(cs)


def first_open_cell(b):
    """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
    cs = open_cells(b)
    if cs != []:
        return cs[0]
    else:
        return None


def get_human_move(board, letter):  	  	  
    """  	  	  
    Ask a human which move to take, or whether they want to quit.  	  	  
    Perform rudimentary input validation, repeating the prompt until a valid  	  	  
    input is given:  	  	  
     * Integers must be in the range of [1..9] (whether it represents a legal  	  	  
       move is to be handled by the caller)  	  	  
     * Strings beginning with 'Q' or 'q' quit the game  	  	  

    Return an integer [1..9] to indicate the move to take, or False to quit the game  	  	  
    """  	  	  
    while True:  	  	  
        show(board)  	  	  
        choice = input("Place your '{}' (or 'Q' to quit)> ".format(color(letter)))  	  	  
        if not choice.isdigit():  	  	  
            if choice.lower().startswith('q'):  	  	  
                return False  	  	  
            else:  	  	  
                print("I don't understand '{}', try again!\n".format(choice))  	  	  
        else:  	  	  
            choice = int(choice)  	  	  
            if not 0 < choice < 10:  	  	  
                print("Numbers must be between 1 and 9, try again!\n")  	  	  
            else:  	  	  
                return choice  	  	  


def make_board():  	  	  
    """  	  	  
    A board is a 3-tuple of 3-tuples, where each tuple is one row  	  	  
    """  	  	  
    return tuple([tuple([1, 2, 3]),  	  	  
                  tuple([4, 5, 6]),  	  	  
                  tuple([7, 8, 9])])  	  	  


def place(board, position, player):  	  	  
    """  	  	  
    Accepts: a game board (tuple), position (integer), and a player's identity ("X" or "O")  	  	  
    Return a copy of the board with that player's mark put into the requested  	  	  
    position, iff a player's mark isn't already present there.  	  	  

    Otherwise, return False  	  	  
    """  	  	  
    if not 1 <= position <= 9:  	  	  
        # player requested an out-of-bounds position  	  	  
        return False  	  	  

    # convert position into (row, col) coordinates  	  	  
    row, col = pos_to_rowcol(position)  	  	  

    if board[row][col] != 'X' and board[row][col] != 'O':  	  	  
        # construct a brand-new board
        new = []  	  	  
        for r in board:  	  	  
            new.append(list(r))  	  	  
        new[row][col] = player  	  	  
        # Always maintain the board as a tuple to guarantee that it  	  	  
        # can never be accidentally modified  	  	  
        return tuple([tuple(new[0]), tuple(new[1]), tuple(new[2])])  	  	  
    else:  	  	  
        return False  	  	  


def horizontal_winner(board):  	  	  
    """  	  	  
    Determines which a player has won a game with a horizontal triple.  	  	  
    Input: a 2D game board.  	  	  
    Return: 'X' or 'O' when there is a winner, or False when no player has 3 in  	  	  
    a horizontal row  	  	  

    The code we arrived at borders on being too clever for our own good, and  	  	  
    bears some explanation.  	  	  

    The first line checks whether the three cells in the top row are all the  	  	  
    same.  This is ONLY true when the same player has played their mark there.  	  	  
    The `and` conjunction at the end of each sub-clause might look useless, but  	  	  
    is very important.  It returns the letter of the winning player:  	  	  
        https://docs.python.org/3/reference/expressions.html#boolean-operations  	  	  

    Without it, this function could only return 'True' or 'False', merely  	  	  
    indicating that SOMEBODY won the game instead of stating who the winner is.  	  	  
    """  	  	  
    return (board[0][0] == board[0][1] == board[0][2] and board[0][2]) \
        or (board[1][0] == board[1][1] == board[1][2] and board[1][2]) \
        or (board[2][0] == board[2][1] == board[2][2] and board[2][2])  	  	  


def vertical_winner(board):  	  	  
    """  	  	  
    Determines which a player has won a game with a vertical triple  	  	  
    """  	  	  
    return (board[0][0] == board[1][0] == board[2][0] and board[2][0]) \
        or (board[0][1] == board[1][1] == board[2][1] and board[2][1]) \
        or (board[0][2] == board[1][2] == board[2][2] and board[2][2])  	  	  


def diagonal_winner(board):  	  	  
    """  	  	  
    Determines which a player has won a game with a diagonal triple  	  	  
    """  	  	  
    return (board[0][0] == board[1][1] == board[2][2] and board[2][2]) \
        or (board[2][0] == board[1][1] == board[0][2] and board[0][2])  	  	  


def pos_to_rowcol(position):  	  	  
    """  	  	  
    Given a TicTacToe board position (int),  	  	  
    Return a tuple(row, col)  	  	  

    Inverse of the function rowcol_to_pos()  	  	  
    """  	  	  
    cell = position - 1  	  	  
    row = cell // 3  	  	  
    col = cell % 3  	  	  
    return row, col  	  	  


def rowcol_to_pos(rowcol):  	  	  
    """  	  	  
    Given a row and column (as a tuple)  	  	  
    Return a TicTacToe board position (int)  	  	  

    Inverse of the function pos_to_rowcol()  	  	  
    """  	  	  
    row = rowcol[0]  	  	  
    col = rowcol[1]  	  	  
    pos = row * 3 + col  	  	  
    return pos + 1  	  	  


def full(board):  	  	  
    return open_cells(board) == ()  	  	  
