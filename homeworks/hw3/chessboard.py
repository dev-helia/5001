'''
Two helper functions to check:
If the row/column is valid or not for the standard chessboard
'''

def check_valid_row(row):
    '''
    Function purpose:
    To check if the row is valid in a chessboard.
    It should be in the range of 1-8.
    
    Parameter:
    row: char/int
        The row you want to check in the chessboard.
        The row should be able to accept integers or strings as parameters.

    Return:
    bool: True if the rowpassed in is valid, False if not.
    '''
    
    # Homogenize the input
    row = int(row)

    # Make decision
    if 1 <= row <= 8:
        return True
    return False

def check_valid_column(column):
    '''
    Function purpose:
    To check if the column is valid in a chessboard.
    It should be a letter from a-h.

    Parameter:
    column: char
        The column you want to check in the chessboard.
        Accept upper or lowercase strings as parameters
    
    Return:
    bool: True if the column passed in is valid, False if not.
    '''
    
    # Homogenize the input
    column = column.lower()

    # Make decision
    if 'a' <= column <= 'h':
        return True
    
    return False
