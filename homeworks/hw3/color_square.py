def black_or_white(row, column):
    '''
    Function purpose:
    Presume the row and column is valid.
    Check whether the square is "BLACK" or "WHITE".

    Parameters:
    column:
        type: char
        The column you want to check in the chessboard.
        The column should accept upper or lowercase strings.
    row:
        type: char/int
        The row you want to check in the chessboard.
        The row should accept integers or strings.

    Return:
    str: "BLACK" or "WHITE" based on the row/column values.
    '''
    # Homogenize the input
    row = int(row)
    column = column.lower()

    # The color depends on whether the sum of row and column index
    column_index = ord(column) - ord('a') + 1

    if (row + column_index) % 2 == 0:
        return "BLACK"
    else:
        return "WHITE"
