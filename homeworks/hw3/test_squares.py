'''
The test functions for check_valid_row() and check_valid_column()
'''

import chessboard

def test_check_valid_row(row, expected):
    '''
    Function purpose:
    To test the function:check_valid_row(row) in chessboard.py
    
    Parameter introduction:
    row: char/int
    The row you want to check in the chessboard.
    The row should be able to accept integers or strings as parameters.

    expected:boolean
    The right answer

    Test cases:
    1 True
    '2' True
    0 False
    10 False
    '''
    result = chessboard.check_valid_row(row)
    print(f'Row: {row}, Expected: {expected}, Actual: {result}')

    
def test_check_valid_column(column, expected):
    '''
    Function purpose:
    To test the function:check_valid_column(column) in chessboard.py
    
    Parameter introduction:
    column: char
    The column you want to check in the chessboard.
    The column should be able to accept upper
    or lowercase strings as parameters
    
    expected:boolean
    The right answer

    Test cases:
    'h' True
    'A' True
    'Z' False
    'p' False
    '''
    result = chessboard.check_valid_column(column)
    print(f'Column: {column}, Expected: {expected}, Actual: {result}')

def test_squares():
    test_check_valid_row(1, True)
    test_check_valid_row('2', True)
    test_check_valid_row(0, False)
    test_check_valid_row(10, False)
    test_check_valid_column('h', True)
    test_check_valid_column('A', True)
    test_check_valid_column('Z', False)
    test_check_valid_column('p', False)
    
